from __future__ import annotations

import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
from typing import Any

from .archive import load_catalog
from .config import ROOT, atomic_write_json, utc_now


PLACEHOLDER_PATTERN = re.compile(r"\b(?:NotImplementedError|TODO|FIXME)\b", re.IGNORECASE)
LANGUAGE_EXTENSIONS = {
    "bash": ".sh",
    "javascript": ".js",
    "mysql": ".sql",
    "python3": ".py",
    "pythondata": ".pythondata",
    "typescript": ".ts",
}


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("JSON 根节点不是对象")
    return value


def audit_coverage(*, root: Path = ROOT) -> dict[str, Any]:
    """Audit the free experiment universe without executing untrusted solutions."""
    catalog = load_catalog(root)
    eligible = [item for item in catalog["problems"] if not item.get("paidOnly")]
    eligible_by_slug = {str(item["titleSlug"]): item for item in eligible}
    problem_root = root / "problems"

    directories_by_slug: dict[str, list[Path]] = {}
    malformed_directories: list[dict[str, str]] = []
    for directory in sorted(path for path in problem_root.iterdir() if path.is_dir()):
        meta_path = directory / "meta.json"
        if not meta_path.is_file():
            malformed_directories.append(
                {"directory": directory.name, "reason": "missing meta.json"}
            )
            continue
        try:
            meta = _read_json(meta_path)
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
            malformed_directories.append(
                {"directory": directory.name, "reason": f"invalid meta.json: {exc}"}
            )
            continue
        slug = str(meta.get("titleSlug") or "")
        if not slug:
            malformed_directories.append(
                {"directory": directory.name, "reason": "meta titleSlug is empty"}
            )
            continue
        directories_by_slug.setdefault(slug, []).append(directory)

    missing_directories = sorted(set(eligible_by_slug) - set(directories_by_slug))
    duplicate_directories = {
        slug: [str(path.relative_to(root)) for path in paths]
        for slug, paths in sorted(directories_by_slug.items())
        if slug in eligible_by_slug and len(paths) > 1
    }

    issues: list[dict[str, Any]] = []
    language_counts: Counter[str] = Counter()
    syntax_checked: Counter[str] = Counter()
    valid_candidates: set[str] = set()
    candidate_hashes: dict[str, str] = {}
    placeholder_slugs: set[str] = set()
    external_syntax_candidates: dict[str, list[tuple[str, Path]]] = {
        "javascript": [],
        "bash": [],
    }
    for slug in sorted(set(eligible_by_slug) & set(directories_by_slug)):
        paths = directories_by_slug[slug]
        if len(paths) != 1:
            continue
        directory = paths[0]
        try:
            meta = _read_json(directory / "meta.json")
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
            continue
        language = str(meta.get("language") or "")
        solution_file = str(meta.get("solutionFile") or "")
        expected_extension = LANGUAGE_EXTENSIONS.get(language)
        language_counts[language or "UNKNOWN"] += 1

        required = ["problem.md", "approach.md", "meta.json"]
        if solution_file:
            required.append(solution_file)
        else:
            issues.append({"slug": slug, "kind": "missing_solution_file_in_meta"})
        missing_or_empty = [
            name
            for name in required
            if not (directory / name).is_file() or (directory / name).stat().st_size == 0
        ]
        if missing_or_empty:
            issues.append(
                {"slug": slug, "kind": "missing_or_empty_files", "files": missing_or_empty}
            )
            continue
        if expected_extension is None:
            issues.append({"slug": slug, "kind": "unsupported_language", "language": language})
            continue
        if Path(solution_file).suffix != expected_extension:
            issues.append(
                {
                    "slug": slug,
                    "kind": "language_extension_mismatch",
                    "language": language,
                    "solutionFile": solution_file,
                }
            )
            continue

        solution_path = directory / solution_file
        try:
            source = solution_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            issues.append({"slug": slug, "kind": "unreadable_solution", "reason": str(exc)})
            continue
        if PLACEHOLDER_PATTERN.search(source):
            placeholder_slugs.add(slug)
            issues.append({"slug": slug, "kind": "placeholder_marker"})
            continue
        if language in {"python3", "pythondata"}:
            try:
                ast.parse(source, filename=str(solution_path))
            except SyntaxError as exc:
                issues.append(
                    {
                        "slug": slug,
                        "kind": "python_syntax_error",
                        "line": exc.lineno,
                        "reason": exc.msg,
                    }
                )
                continue
            syntax_checked[language] += 1
        elif language in external_syntax_candidates:
            external_syntax_candidates[language].append((slug, solution_path))
        valid_candidates.add(slug)
        candidate_hashes[slug] = hashlib.sha256(source.encode("utf-8")).hexdigest()

    syntax_gate_availability = {
        "javascript": bool(shutil.which("node")),
        "bash": bool(shutil.which("sh")),
        "typescript": bool(shutil.which("tsc")),
        "mysql": False,
    }
    syntax_gate_skipped = Counter(
        {
            language: language_counts[language]
            for language in ("bash", "typescript", "mysql")
            if language_counts[language] and not syntax_gate_availability[language]
        }
    )
    for language, candidates in external_syntax_candidates.items():
        executable = "node" if language == "javascript" else "sh"
        if not syntax_gate_availability[language]:
            continue
        for slug, solution_path in candidates:
            command = (
                [executable, "--check", str(solution_path)]
                if language == "javascript"
                else [executable, "-n", str(solution_path)]
            )
            result = subprocess.run(command, capture_output=True, text=True, timeout=10)
            if result.returncode:
                valid_candidates.discard(slug)
                candidate_hashes.pop(slug, None)
                issues.append(
                    {
                        "slug": slug,
                        "kind": f"{language}_syntax_error",
                        "reason": (result.stderr or result.stdout).strip(),
                    }
                )
            else:
                syntax_checked[language] += 1

    return {
        "schemaVersion": 1,
        "generatedAt": utc_now(),
        "eligibleProblems": len(eligible),
        "directoriesPresent": len(set(eligible_by_slug) & set(directories_by_slug)),
        "validLocalCandidates": len(valid_candidates),
        "invalidLocalCandidates": len(eligible) - len(valid_candidates),
        "languageCounts": dict(sorted(language_counts.items())),
        "syntaxChecked": dict(sorted(syntax_checked.items())),
        "syntaxGateAvailability": syntax_gate_availability,
        "syntaxGateSkipped": dict(sorted(syntax_gate_skipped.items())),
        "missingDirectories": missing_directories,
        "duplicateDirectories": duplicate_directories,
        "malformedDirectories": malformed_directories,
        "placeholderSlugs": sorted(placeholder_slugs),
        "candidateCodeSha256": dict(sorted(candidate_hashes.items())),
        "issues": issues,
        "policy": (
            "本地候选仅表示目录、必要文件、语言映射、占位标记与可用静态语法门禁通过；"
            "可用原语言门禁会执行；缺少本机检查器的语言仅做文件和占位静态门禁。"
            "本地候选不等于远程 Accepted。"
        ),
    }


def write_coverage(*, root: Path = ROOT) -> dict[str, Any]:
    report = audit_coverage(root=root)
    atomic_write_json(root / "stats" / "coverage.json", report)
    return report
