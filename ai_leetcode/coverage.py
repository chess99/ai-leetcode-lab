from __future__ import annotations

import ast
from collections import Counter
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import tokenize
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


def _fill_empty_python_function_bodies(source: str) -> str:
    """Make archived LeetCode Python templates parseable without changing semantics.

    LeetCode leaves function bodies blank in its snippets.  The terminating colon
    may be on a later line, so token positions are used instead of a line regex.
    """
    lines = source.splitlines()
    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
    insert_after: dict[int, str] = {}
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token.type != tokenize.NAME or token.string not in {"def", "async"}:
            index += 1
            continue
        if token.string == "async":
            next_index = index + 1
            if (
                next_index >= len(tokens)
                or tokens[next_index].type != tokenize.NAME
                or tokens[next_index].string != "def"
            ):
                index += 1
                continue
            def_token = tokens[next_index]
            index = next_index
        else:
            def_token = token

        depth = 0
        colon = None
        cursor = index + 1
        while cursor < len(tokens):
            current = tokens[cursor]
            if current.type == tokenize.OP:
                if current.string in "([{":
                    depth += 1
                elif current.string in ")]}" and depth:
                    depth -= 1
                elif current.string == ":" and depth == 0:
                    colon = current
                    break
            cursor += 1
        if colon is None:
            index += 1
            continue

        colon_line = colon.end[0]
        inline_tail = lines[colon_line - 1][colon.end[1] :].strip()
        if inline_tail and not inline_tail.startswith("#"):
            index = cursor + 1
            continue

        next_line = colon_line + 1
        while next_line <= len(lines):
            stripped = lines[next_line - 1].strip()
            if stripped and not stripped.startswith("#"):
                break
            next_line += 1
        next_indent = (
            len(lines[next_line - 1]) - len(lines[next_line - 1].lstrip(" \t"))
            if next_line <= len(lines)
            else -1
        )
        if next_indent <= def_token.start[1]:
            prefix = lines[def_token.start[0] - 1][: def_token.start[1]]
            insert_after[colon_line] = f"{prefix}    pass"
        index = cursor + 1

    output: list[str] = []
    for line_number, line in enumerate(lines, start=1):
        output.append(line)
        if line_number in insert_after:
            output.append(insert_after[line_number])
    return "\n".join(output) + ("\n" if source.endswith(("\n", "\r")) else "")


def _method_is_static(method: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    for decorator in method.decorator_list:
        target = decorator.func if isinstance(decorator, ast.Call) else decorator
        if isinstance(target, ast.Name) and target.id == "staticmethod":
            return True
        if isinstance(target, ast.Attribute) and target.attr == "staticmethod":
            return True
    return False


def _bound_positional_range(
    method: ast.FunctionDef | ast.AsyncFunctionDef,
) -> tuple[int, int | None, bool]:
    positional = [*method.args.posonlyargs, *method.args.args]
    bound = 0 if _method_is_static(method) or not positional else 1
    required = max(0, len(positional) - len(method.args.defaults) - bound)
    maximum = None if method.args.vararg is not None else max(0, len(positional) - bound)
    required_keyword_only = any(
        default is None for default in method.args.kw_defaults
    )
    return required, maximum, required_keyword_only


def _python_template_interface(source: str) -> tuple[str, dict[str, int]]:
    tree = ast.parse(_fill_empty_python_function_bodies(source))
    classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    if not classes:
        raise ValueError("Python3 模板没有顶层类")
    expected_class = classes[-1]
    methods: dict[str, int] = {}
    for node in expected_class.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.name.startswith("_") and node.name != "__init__":
            continue
        positional = [*node.args.posonlyargs, *node.args.args]
        bound = 0 if _method_is_static(node) or not positional else 1
        methods[node.name] = max(0, len(positional) - bound)
    return expected_class.name, methods


def _python_interface_issue(
    *, template_source: str, candidate_tree: ast.Module, slug: str
) -> dict[str, Any] | None:
    expected_class, expected_methods = _python_template_interface(template_source)
    classes = [node for node in candidate_tree.body if isinstance(node, ast.ClassDef)]
    matching = next((node for node in classes if node.name == expected_class), None)
    if matching is None:
        return {
            "slug": slug,
            "kind": "python_interface_class_mismatch",
            "expectedClass": expected_class,
            "foundClasses": [node.name for node in classes],
        }

    actual_methods = {
        node.name: node
        for node in matching.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    missing = sorted(set(expected_methods) - set(actual_methods))
    if missing:
        return {
            "slug": slug,
            "kind": "python_interface_methods_missing",
            "class": expected_class,
            "methods": missing,
        }

    incompatible: list[dict[str, Any]] = []
    for method_name, expected_arguments in sorted(expected_methods.items()):
        minimum, maximum, needs_keywords = _bound_positional_range(actual_methods[method_name])
        if (
            needs_keywords
            or expected_arguments < minimum
            or (maximum is not None and expected_arguments > maximum)
        ):
            incompatible.append(
                {
                    "method": method_name,
                    "judgeArguments": expected_arguments,
                    "acceptedPositionalMinimum": minimum,
                    "acceptedPositionalMaximum": maximum,
                    "requiredKeywordOnly": needs_keywords,
                }
            )
    if incompatible:
        return {
            "slug": slug,
            "kind": "python_interface_arity_mismatch",
            "class": expected_class,
            "methods": incompatible,
        }
    return None


def _archived_python3_template(root: Path, directory: Path) -> str | None:
    archive_path = root / "archive" / "problems" / f"{directory.name}.json"
    if not archive_path.is_file():
        return None
    archive = _read_json(archive_path)
    question = archive.get("question")
    if not isinstance(question, dict):
        raise ValueError("归档缺少 question 对象")
    snippets = question.get("codeSnippets")
    if not isinstance(snippets, list):
        raise ValueError("归档缺少 codeSnippets 数组")
    for snippet in snippets:
        if isinstance(snippet, dict) and snippet.get("langSlug") == "python3":
            code = snippet.get("code")
            if isinstance(code, str) and code.strip():
                return code
            raise ValueError("归档 Python3 模板为空")
    raise ValueError("归档缺少 Python3 模板")


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
    interface_checked: Counter[str] = Counter()
    interface_gate_skipped: Counter[str] = Counter()
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
                candidate_tree = ast.parse(source, filename=str(solution_path))
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
            if language == "python3":
                try:
                    template_source = _archived_python3_template(root, directory)
                    if template_source is None:
                        interface_gate_skipped["missing_archive"] += 1
                    else:
                        interface_issue = _python_interface_issue(
                            template_source=template_source,
                            candidate_tree=candidate_tree,
                            slug=slug,
                        )
                        interface_checked[language] += 1
                        if interface_issue is not None:
                            issues.append(interface_issue)
                            continue
                except (OSError, UnicodeError, json.JSONDecodeError, ValueError, SyntaxError) as exc:
                    issues.append(
                        {
                            "slug": slug,
                            "kind": "python_interface_template_error",
                            "reason": str(exc),
                        }
                    )
                    continue
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
        "interfaceChecked": dict(sorted(interface_checked.items())),
        "interfaceGateSkipped": dict(sorted(interface_gate_skipped.items())),
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
            "Python3 候选还会与归档判题模板核对顶层类、公开方法和位置参数数量；"
            "可用原语言门禁会执行；缺少本机检查器的语言仅做文件和占位静态门禁。"
            "本地候选不等于远程 Accepted。"
        ),
    }


def write_coverage(*, root: Path = ROOT) -> dict[str, Any]:
    report = audit_coverage(root=root)
    atomic_write_json(root / "stats" / "coverage.json", report)
    return report
