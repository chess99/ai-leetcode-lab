from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
from typing import Any

from .archive import load_catalog
from .config import AttemptBudget, ROOT, atomic_write_json, atomic_write_text, utc_now
from .events import EventStore


def build_summary(budget: AttemptBudget, *, root: Path = ROOT) -> dict[str, Any]:
    catalog = load_catalog(root)
    problems = catalog["problems"]
    by_slug = {item["titleSlug"]: item for item in problems}
    events = EventStore(root).load()
    started = {event["slug"] for event in events if event.get("type") == "problem_started"}
    accepted_events = [
        event
        for event in events
        if event.get("type") == "submission_result" and event.get("outcome") == "accepted"
    ]
    accepted_by_slug: dict[str, dict[str, Any]] = {}
    for event in accepted_events:
        accepted_by_slug.setdefault(str(event["slug"]), event)
    accepted = set(accepted_by_slug)
    submission_starts = [event for event in events if event.get("type") == "submission_started"]
    test_starts = [event for event in events if event.get("type") == "remote_test_started"]
    review_required: set[str] = set()
    store = EventStore(root)
    for slug in started - accepted:
        usage = store.usage(slug)
        if usage.round_number >= budget.max_rounds and usage.submissions >= budget.submissions_per_round:
            review_required.add(slug)

    difficulty_total = Counter(str(item.get("difficulty", "UNKNOWN")) for item in problems)
    difficulty_accepted = Counter(
        str(by_slug[slug].get("difficulty", "UNKNOWN")) for slug in accepted if slug in by_slug
    )
    accepted_by_model = Counter(
        f"{event.get('client', 'unknown')} / {event.get('model', 'unknown')}" for event in accepted_by_slug.values()
    )
    first_submission_accepts = sum(
        1
        for event in accepted_by_slug.values()
        if int(event.get("round", 0)) == 1 and int(event.get("attempt", 0)) == 1
    )
    first_round_accepts = sum(1 for event in accepted_by_slug.values() if int(event.get("round", 0)) == 1)
    archived_files = list((root / "archive" / "problems").glob("*.json"))
    readable_archives = 0
    for path in archived_files:
        try:
            question = json.loads(path.read_text(encoding="utf-8")).get("question") or {}
            if question.get("translatedContent") or question.get("content"):
                readable_archives += 1
        except (OSError, json.JSONDecodeError, AttributeError):
            continue
    archived = len(archived_files)
    total = len(problems)
    accessible = sum(1 for item in problems if not item.get("paidOnly"))
    accepted_count = len(accepted)
    return {
        "schemaVersion": 1,
        "generatedAt": utc_now(),
        "catalogSyncedAt": catalog.get("syncedAt"),
        "catalogTotal": total,
        "accessibleWithoutPremium": accessible,
        "paidOnly": total - accessible,
        "archivedDetails": archived,
        "archivedReadableDetails": readable_archives,
        "archivedLockedOrUnavailable": archived - readable_archives,
        "started": len(started),
        "accepted": accepted_count,
        "reviewRequired": len(review_required),
        "remainingAccessible": max(accessible - accepted_count, 0),
        "remoteTests": len(test_starts),
        "submissions": len(submission_starts),
        "firstSubmissionAccepted": first_submission_accepts,
        "firstRoundAccepted": first_round_accepts,
        "firstSubmissionAcceptanceRate": first_submission_accepts / accepted_count if accepted_count else 0.0,
        "overallSubmissionAcceptanceRate": accepted_count / len(submission_starts) if submission_starts else 0.0,
        "byDifficulty": {
            level: {"total": difficulty_total[level], "accepted": difficulty_accepted[level]}
            for level in sorted(difficulty_total)
        },
        "acceptedByAgent": dict(sorted(accepted_by_model.items())),
        "reviewRequiredSlugs": sorted(review_required),
    }


def render_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# AI 刷题实验统计",
        "",
        f"更新时间：{summary['generatedAt']}",
        "",
        "## 总览",
        "",
        "| 指标 | 数量 |",
        "|---|---:|",
        f"| 题库总数 | {summary['catalogTotal']} |",
        f"| 免费可做 | {summary['accessibleWithoutPremium']} |",
        f"| 付费题 | {summary['paidOnly']} |",
        f"| 已归档完整题面 | {summary['archivedDetails']} |",
        f"| 归档中可读题面 | {summary['archivedReadableDetails']} |",
        f"| 归档中锁定/不可用题面 | {summary['archivedLockedOrUnavailable']} |",
        f"| 已开始 | {summary['started']} |",
        f"| Accepted | {summary['accepted']} |",
        f"| 等待人工复盘 | {summary['reviewRequired']} |",
        f"| 远程试跑 | {summary['remoteTests']} |",
        f"| 正式提交 | {summary['submissions']} |",
        "",
        "## 通过质量",
        "",
        f"- 首次提交通过：{summary['firstSubmissionAccepted']}",
        f"- 第一轮内通过：{summary['firstRoundAccepted']}",
        f"- 首投通过占已通过题比例：{summary['firstSubmissionAcceptanceRate']:.2%}",
        f"- 正式提交整体通过率：{summary['overallSubmissionAcceptanceRate']:.2%}",
        "",
        "## 难度分布",
        "",
        "| 难度 | 总数 | 已通过 |",
        "|---|---:|---:|",
    ]
    for level, values in summary["byDifficulty"].items():
        lines.append(f"| {level} | {values['total']} | {values['accepted']} |")
    lines.extend(["", "## Agent 贡献", ""])
    if summary["acceptedByAgent"]:
        for name, count in summary["acceptedByAgent"].items():
            lines.append(f"- {name}: {count}")
    else:
        lines.append("尚无 Accepted 记录。")
    if summary["reviewRequiredSlugs"]:
        lines.extend(["", "## 等待人工复盘", ""])
        lines.extend(f"- {slug}" for slug in summary["reviewRequiredSlugs"])
    lines.append("")
    return "\n".join(lines)


def write_stats(budget: AttemptBudget, *, root: Path = ROOT) -> dict[str, Any]:
    summary = build_summary(budget, root=root)
    atomic_write_json(root / "stats" / "summary.json", summary)
    atomic_write_text(root / "stats" / "summary.md", render_markdown(summary))
    return summary
