from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Callable

from .client import LeetCodeClient
from .config import (
    ExperimentConfig,
    Identity,
    LANGUAGE_EXTENSIONS,
    ROOT,
    atomic_write_json,
    atomic_write_text,
    problem_key,
    utc_now,
)
from .events import EventStore


class ArchiveError(RuntimeError):
    """Raised when catalog or archived question data is unavailable."""


def catalog_path(root: Path = ROOT) -> Path:
    return root / "archive" / "catalog.json"


def normalize_question(raw: dict[str, Any]) -> dict[str, Any]:
    tags = [
        {
            "name": tag.get("name"),
            "translatedName": tag.get("nameTranslated") or tag.get("translatedName"),
            "slug": tag.get("slug"),
        }
        for tag in raw.get("topicTags") or []
    ]
    return {
        "id": raw.get("id"),
        "questionFrontendId": str(raw.get("questionFrontendId", "")),
        "title": raw.get("title"),
        "translatedTitle": raw.get("translatedTitle"),
        "titleSlug": raw.get("titleSlug"),
        "difficulty": raw.get("difficulty"),
        "paidOnly": bool(raw.get("paidOnly", False)),
        "status": raw.get("status"),
        "acRate": raw.get("acRate"),
        "frequency": raw.get("frequency"),
        "contestPoint": raw.get("contestPoint"),
        "topicTags": tags,
    }


def sync_catalog(
    client: LeetCodeClient,
    config: ExperimentConfig,
    *,
    authenticated: bool,
    root: Path = ROOT,
    progress: Callable[[str], None] = print,
) -> dict[str, Any]:
    skip = 0
    questions: list[dict[str, Any]] = []
    total = 0
    finished = 0
    while True:
        page = client.list_questions(skip, config.archive.page_size, authenticated=authenticated)
        batch = page.get("questions") or []
        if not isinstance(batch, list):
            raise ArchiveError("题库列表 questions 不是数组")
        questions.extend(normalize_question(item) for item in batch)
        total = int(page.get("totalLength") or len(questions))
        finished = int(page.get("finishedLength") or 0)
        progress(f"目录同步：{len(questions)}/{total}")
        if not page.get("hasMore") or not batch:
            break
        skip += len(batch)

    by_slug: dict[str, dict[str, Any]] = {}
    for question in questions:
        slug = str(question.get("titleSlug") or "")
        if not slug:
            raise ArchiveError("题目缺少 titleSlug")
        by_slug[slug] = question
    if total and len(by_slug) != total:
        raise ArchiveError(f"目录数量不一致：接口 {total}，去重后 {len(by_slug)}")
    ordered = sorted(
        by_slug.values(),
        key=lambda item: (0, int(item["questionFrontendId"]))
        if str(item["questionFrontendId"]).isdigit()
        else (1, str(item["questionFrontendId"]), str(item["titleSlug"])),
    )
    catalog = {
        "schemaVersion": 1,
        "source": f"{config.endpoint}/problemset/",
        "syncedAt": utc_now(),
        "total": len(ordered),
        "finishedOnAccount": finished,
        "problems": ordered,
    }
    atomic_write_json(catalog_path(root), catalog)
    return catalog


def load_catalog(root: Path = ROOT) -> dict[str, Any]:
    path = catalog_path(root)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ArchiveError("题库目录尚未同步，请先运行 sync") from exc
    except json.JSONDecodeError as exc:
        raise ArchiveError(f"题库目录 JSON 损坏：{exc}") from exc
    if not isinstance(value, dict) or not isinstance(value.get("problems"), list):
        raise ArchiveError("题库目录结构无效")
    return value


def resolve_problem(selector: str, root: Path = ROOT) -> dict[str, Any]:
    selector_normalized = selector.strip().lower()
    matches: list[dict[str, Any]] = []
    for problem in load_catalog(root)["problems"]:
        candidates = {
            str(problem.get("titleSlug", "")).lower(),
            str(problem.get("questionFrontendId", "")).lower(),
            str(problem.get("id", "")).lower(),
        }
        if selector_normalized in candidates:
            matches.append(problem)
    if not matches:
        raise ArchiveError(f"题库中找不到：{selector}")
    slug_matches = [item for item in matches if str(item["titleSlug"]).lower() == selector_normalized]
    if len(slug_matches) == 1:
        return slug_matches[0]
    if len(matches) > 1:
        labels = ", ".join(f"{item['questionFrontendId']}:{item['titleSlug']}" for item in matches)
        raise ArchiveError(f"选择器不唯一：{selector} -> {labels}；请改用 slug")
    return matches[0]


def detail_path(problem: dict[str, Any], root: Path = ROOT) -> Path:
    return root / "archive" / "problems" / f"{problem_key(problem)}.json"


def load_detail(problem: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    path = detail_path(problem, root)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ArchiveError(f"题面尚未归档：{problem['titleSlug']}") from exc
    except json.JSONDecodeError as exc:
        raise ArchiveError(f"题面归档损坏：{path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ArchiveError(f"题面归档结构无效：{path}")
    return value


def archive_detail(
    client: LeetCodeClient,
    problem: dict[str, Any],
    *,
    authenticated: bool,
    root: Path = ROOT,
) -> dict[str, Any]:
    question = client.get_question(str(problem["titleSlug"]), authenticated=authenticated)
    # 为保持实验独立性，归档只保留题面与代码模板，不保存官方提示或相似题推荐。
    question.pop("hints", None)
    question.pop("similarQuestions", None)
    value = {
        "schemaVersion": 1,
        "archivedAt": utc_now(),
        "source": f"{client.config.endpoint}/problems/{problem['titleSlug']}/",
        "question": question,
    }
    atomic_write_json(detail_path(problem, root), value)
    return value


def sync_details(
    client: LeetCodeClient,
    config: ExperimentConfig,
    catalog: dict[str, Any],
    *,
    authenticated: bool,
    refresh: bool = False,
    detail_limit: int | None = None,
    root: Path = ROOT,
    progress: Callable[[str], None] = print,
) -> dict[str, int]:
    problems = list(catalog["problems"])
    pending = [item for item in problems if refresh or not detail_path(item, root).exists()]
    if detail_limit is not None:
        pending = pending[: max(0, detail_limit)]
    skipped = len(problems) - len(pending)
    if not pending:
        progress("题面归档已是最新，无需下载")
        return {"downloaded": 0, "failed": 0, "skipped": skipped}

    def fetch(item: dict[str, Any]) -> tuple[str, str | None]:
        try:
            archive_detail(client, item, authenticated=authenticated, root=root)
            time.sleep(config.archive.request_delay_ms / 1000)
            return str(item["titleSlug"]), None
        except Exception as exc:  # errors are summarized and the sync remains resumable
            return str(item["titleSlug"]), str(exc)

    downloaded = 0
    failures: list[tuple[str, str]] = []
    with ThreadPoolExecutor(max_workers=config.archive.concurrency) as executor:
        futures = {executor.submit(fetch, item): item for item in pending}
        for future in as_completed(futures):
            slug, error = future.result()
            if error:
                failures.append((slug, error))
            else:
                downloaded += 1
            done = downloaded + len(failures)
            if done == 1 or done % 50 == 0 or done == len(pending):
                progress(f"题面归档：{done}/{len(pending)}，成功 {downloaded}，失败 {len(failures)}")

    if failures:
        failure_log = root / ".runtime" / "sync-failures.json"
        atomic_write_json(
            failure_log,
            {"generatedAt": utc_now(), "failures": [{"slug": slug, "error": error} for slug, error in failures]},
        )
        progress(f"失败清单已保存到 {failure_log}")
    return {"downloaded": downloaded, "failed": len(failures), "skipped": skipped}


def _comment_prefix(extension: str) -> str:
    return "#" if extension in {"py", "rb", "sh"} else "--" if extension == "sql" else "//"


def _problem_markdown(problem: dict[str, Any], question: dict[str, Any], endpoint: str) -> str:
    title = question.get("translatedTitle") or question.get("title") or problem["titleSlug"]
    content = question.get("translatedContent") or question.get("content")
    if not content:
        content = "> 当前账号无法读取完整题面（可能是付费题）。"
    tags = question.get("topicTags") or problem.get("topicTags") or []
    tag_names = [tag.get("translatedName") or tag.get("name") for tag in tags]
    lines = [
        f"# {problem.get('questionFrontendId')}. {title}",
        "",
        f"- 难度：{problem.get('difficulty')}",
        f"- 标签：{', '.join(str(item) for item in tag_names if item) or '无'}",
        f"- 来源：{endpoint}/problems/{problem['titleSlug']}/",
        f"- 归档：{utc_now()}",
        "",
        "## 题目",
        "",
        str(content),
        "",
        "## 样例输入",
        "",
        "```text",
        str(question.get("sampleTestCase") or question.get("exampleTestcases") or ""),
        "```",
        "",
    ]
    return "\n".join(lines)


def materialize_problem(
    problem: dict[str, Any],
    detail: dict[str, Any],
    config: ExperimentConfig,
    identity: Identity,
    events: EventStore,
    *,
    language: str,
    root: Path = ROOT,
) -> Path:
    question = detail.get("question") or {}
    snippets = {item.get("langSlug"): item for item in question.get("codeSnippets") or []}
    if language not in snippets:
        available = ", ".join(sorted(str(item) for item in snippets))
        raise ArchiveError(f"题目不支持语言 {language}；可用：{available}")
    extension = LANGUAGE_EXTENSIONS.get(language, language)
    directory = root / "problems" / problem_key(problem)
    meta_path = directory / "meta.json"
    if meta_path.exists():
        return directory
    if directory.exists() and any(directory.iterdir()):
        raise ArchiveError(f"题目目录已存在但缺少 meta.json，拒绝覆盖：{directory}")
    directory.mkdir(parents=True, exist_ok=True)
    solution_name = f"solution.{extension}"
    prefix = _comment_prefix(extension)
    header = "\n".join(
        [
            f"{prefix} AI solution attribution",
            f"{prefix} Client: {identity.client}",
            f"{prefix} Model: {identity.model}",
            f"{prefix} Reasoning effort: {identity.reasoning_effort}",
            f"{prefix} Profile: {identity.profile_id}",
            f"{prefix} Created: {utc_now()}",
            f"{prefix} Experiment: ai-leetcode-lab, round 1",
            "",
        ]
    )
    atomic_write_text(directory / solution_name, header + str(snippets[language].get("code") or "") + "\n")
    atomic_write_text(directory / "problem.md", _problem_markdown(problem, question, config.endpoint))
    atomic_write_text(
        directory / "approach.md",
        "# 解题记录\n\n"
        f"- AI 客户端：{identity.client}\n"
        f"- 模型：{identity.model}\n"
        f"- 推理档位：{identity.reasoning_effort}\n"
        f"- Profile：{identity.profile_id}\n"
        "- 轮次：1\n\n"
        "## 思路\n\n待填写。\n\n"
        "## 复杂度\n\n待填写。\n\n"
        "## 边界条件与本地验证\n\n待填写。\n",
    )
    meta = {
        "schemaVersion": 1,
        "id": problem.get("id"),
        "questionId": question.get("questionId") or problem.get("id"),
        "questionFrontendId": problem.get("questionFrontendId"),
        "titleSlug": problem.get("titleSlug"),
        "title": problem.get("title"),
        "translatedTitle": problem.get("translatedTitle"),
        "difficulty": problem.get("difficulty"),
        "paidOnly": problem.get("paidOnly"),
        "language": language,
        "solutionFile": solution_name,
        "source": f"{config.endpoint}/problems/{problem['titleSlug']}/",
        "createdAt": utc_now(),
        "createdBy": {
            "client": identity.client,
            "model": identity.model,
            "reasoningEffort": identity.reasoning_effort,
            "profileId": identity.profile_id,
        },
    }
    atomic_write_json(meta_path, meta)
    events.append(
        "problem_started",
        slug=problem["titleSlug"],
        question_id=str(meta["questionId"]),
        frontend_id=str(problem.get("questionFrontendId", "")),
        language=language,
        client=identity.client,
        model=identity.model,
        reasoning_effort=identity.reasoning_effort,
        profile_id=identity.profile_id,
    )
    return directory
