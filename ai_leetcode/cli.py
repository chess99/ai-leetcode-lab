from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

from .archive import (
    ArchiveError,
    archive_detail,
    detail_path,
    load_catalog,
    load_detail,
    materialize_problem,
    resolve_problem,
    sync_catalog,
    sync_details,
)
from .client import ApiError, LeetCodeClient
from .config import (
    ConfigError,
    ROOT,
    load_config,
    load_credentials,
    load_identity,
    load_profiles,
    problem_key,
)
from .coverage import audit_coverage, write_coverage
from .doctor import print_checks, run_doctor
from .events import BudgetError, EventStore
from .quota import submission_quota_status
from .runner import (
    RemoteActionLock,
    _python_template_for_problem,
    _validate_submission_source,
    run_remote_test,
    submit_solution,
)
from .stats import build_summary, write_stats


def _client(config: Any, *, credentials_required: bool) -> LeetCodeClient:
    credentials = load_credentials(ROOT, required=credentials_required)
    return LeetCodeClient(config, credentials)


def _print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def _identity(args: argparse.Namespace, *, required: bool = True):
    return load_identity(required=required, profile_id=getattr(args, "profile", None))


def _cmd_doctor(args: argparse.Namespace) -> int:
    config = load_config()
    return 0 if print_checks(run_doctor(config, offline=args.offline, profile_id=args.profile)) else 1


def _cmd_sync(args: argparse.Namespace) -> int:
    config = load_config()
    credentials = load_credentials(ROOT, required=False)
    client = LeetCodeClient(config, credentials)
    catalog = sync_catalog(client, config, authenticated=credentials is not None)
    print(f"题库目录已保存：{catalog['total']} 题")
    if args.with_content:
        result = sync_details(
            client,
            config,
            catalog,
            authenticated=credentials is not None,
            refresh=args.refresh,
            detail_limit=args.detail_limit,
        )
        _print_json(result)
        return 1 if result["failed"] else 0
    return 0


def _eligible(problem: dict[str, Any], difficulty: str | None, include_paid: bool) -> bool:
    return (not difficulty or str(problem.get("difficulty", "")).lower() == difficulty.lower()) and (
        include_paid or not problem.get("paidOnly")
    )


def _cmd_next(args: argparse.Namespace) -> int:
    identity = _identity(args)
    assert identity is not None
    catalog = load_catalog()
    store = EventStore()
    events = store.effective_events()
    started = {
        event.get("slug")
        for event in events
        if event.get("type") in {"problem_started", "profile_started"}
        and event.get("profile_id") == identity.profile_id
    }
    accepted = {
        event.get("slug")
        for event in events
        if event.get("type") == "submission_result" and event.get("outcome") == "accepted"
    }
    deferred: set[str] = set()
    candidate_hashes: dict[str, str] = {}
    for event in events:
        if event.get("profile_id") != identity.profile_id or not event.get("slug"):
            continue
        if event.get("type") == "profile_deferred":
            deferred.add(str(event["slug"]))
        elif event.get("type") == "profile_resumed":
            deferred.discard(str(event["slug"]))
        if (
            event.get("type") == "candidate_ready"
            and event.get("profile_id") == identity.profile_id
            and event.get("slug")
        ):
            candidate_hashes[str(event["slug"])] = str(event.get("code_sha256") or "")

    def candidate_matches(item: dict[str, Any]) -> bool:
        if not args.candidate_ready_only:
            return True
        slug = str(item["titleSlug"])
        expected = candidate_hashes.get(slug)
        if not expected:
            return False
        directory = ROOT / "problems" / problem_key(item)
        try:
            meta = json.loads((directory / "meta.json").read_text(encoding="utf-8"))
            code = (directory / str(meta["solutionFile"])).read_text(encoding="utf-8")
        except (FileNotFoundError, KeyError, json.JSONDecodeError):
            return False
        return hashlib.sha256(code.encode("utf-8")).hexdigest() == expected
    active = [
        item
        for item in catalog["problems"]
        if item["titleSlug"] in started - accepted - deferred
        and _eligible(item, args.difficulty, args.include_paid)
        and candidate_matches(item)
    ]
    candidates = active or [
        item
        for item in catalog["problems"]
        if item["titleSlug"] not in (started | accepted | deferred)
        and _eligible(item, args.difficulty, args.include_paid)
        and candidate_matches(item)
    ]
    if not candidates:
        print("没有符合条件的未完成题目")
        return 1
    problem = candidates[0]
    print(
        f"{problem['questionFrontendId']} {problem.get('translatedTitle') or problem.get('title')} "
        f"[{problem.get('difficulty')}] {problem['titleSlug']}"
    )
    return 0


def _cmd_start(args: argparse.Namespace) -> int:
    config = load_config()
    identity = _identity(args, required=config.identity_required)
    assert identity is not None
    problem = resolve_problem(args.selector)
    store = EventStore()
    if detail_path(problem).exists():
        detail = load_detail(problem)
    else:
        credentials = load_credentials(required=False)
        detail = archive_detail(
            LeetCodeClient(config, credentials),
            problem,
            authenticated=credentials is not None,
        )
    directory = materialize_problem(
        problem,
        detail,
        config,
        identity,
        store,
        language=args.language or config.default_language,
    )
    meta = json.loads((directory / "meta.json").read_text(encoding="utf-8"))
    store.ensure_profile_started(problem, str(meta["language"]), identity)
    print(directory)
    return 0


def _test_input(args: argparse.Namespace) -> str | None:
    if args.input is not None and args.input_file is not None:
        raise ConfigError("--input 与 --input-file 只能使用一个")
    if args.input_file is not None:
        return Path(args.input_file).read_text(encoding="utf-8")
    return args.input.replace("\\n", "\n") if args.input is not None else None


def _cmd_test(args: argparse.Namespace) -> int:
    config = load_config()
    identity = _identity(args)
    assert identity is not None
    result = run_remote_test(
        args.selector,
        _test_input(args),
        _client(config, credentials_required=True),
        config,
        identity,
        EventStore(),
    )
    _print_json(result)
    return 0 if result.get("outcome") == "passed" else 2


def _cmd_submit(args: argparse.Namespace) -> int:
    config = load_config()
    identity = _identity(args)
    assert identity is not None
    result = submit_solution(
        args.selector,
        _client(config, credentials_required=True),
        config,
        identity,
        EventStore(),
        account_reconciliation=args.account_reconciliation,
    )
    _print_json(result)
    if not args.defer_stats:
        write_stats(config.attempt_budget)
    return 0 if result.get("outcome") == "accepted" else 2


def _cmd_retry(args: argparse.Namespace) -> int:
    config = load_config()
    identity = _identity(args)
    assert identity is not None
    problem = resolve_problem(args.selector)
    with RemoteActionLock():
        event = EventStore().open_retry(str(problem["titleSlug"]), args.reason, config.attempt_budget, identity)
    _print_json(event)
    return 0


def _cmd_defer(args: argparse.Namespace) -> int:
    identity = _identity(args)
    assert identity is not None
    problem = resolve_problem(args.selector)
    event = EventStore().defer_profile(str(problem["titleSlug"]), args.reason, identity)
    _print_json(event)
    return 0


def _cmd_resume(args: argparse.Namespace) -> int:
    identity = _identity(args)
    assert identity is not None
    problem = resolve_problem(args.selector)
    event = EventStore().resume_profile(str(problem["titleSlug"]), args.reason, identity)
    _print_json(event)
    return 0


def _cmd_annotate_profile(args: argparse.Namespace) -> int:
    identity = _identity(args)
    assert identity is not None
    problem = resolve_problem(args.selector)
    slug = str(problem["titleSlug"])
    store = EventStore()
    event_ids = list(args.event_id or [])
    if args.all_existing:
        event_ids.extend(
            str(event["event_id"])
            for event in store.load()
            if event.get("slug") == slug and event.get("type") != "profile_annotation"
        )
    event = store.annotate_profile(slug, event_ids, identity, args.reason)
    _print_json(event)
    return 0


def _cmd_annotate_result(args: argparse.Namespace) -> int:
    problem = resolve_problem(args.selector)
    slug = str(problem["titleSlug"])
    event = EventStore().annotate_result(
        slug,
        args.event_id,
        outcome=args.outcome,
        counts_against_budget=args.counts_against_budget,
        classification=args.classification,
        reason=args.reason,
    )
    _print_json(event)
    return 0


def _cmd_report_usage(args: argparse.Namespace) -> int:
    identity = _identity(args)
    assert identity is not None
    problem = resolve_problem(args.selector)
    event = EventStore().report_usage(
        str(problem["titleSlug"]),
        identity,
        source=args.source,
        input_tokens=args.input_tokens,
        output_tokens=args.output_tokens,
        cached_input_tokens=args.cached_input_tokens,
        elapsed_seconds=args.elapsed_seconds,
    )
    _print_json(event)
    return 0


def _cmd_candidate_ready(args: argparse.Namespace) -> int:
    identity = _identity(args)
    assert identity is not None
    problem = resolve_problem(args.selector)
    directory = ROOT / "problems" / problem_key(problem)
    try:
        meta = json.loads((directory / "meta.json").read_text(encoding="utf-8"))
        code = (directory / str(meta["solutionFile"])).read_text(encoding="utf-8")
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as exc:
        raise ConfigError(f"无法读取本地候选：{directory}") from exc
    if "NotImplementedError" in code or "TODO" in code or "FIXME" in code:
        raise ConfigError("占位解答不能记录为 candidate-ready")
    _validate_submission_source(
        str(meta["language"]),
        code,
        template_source=_python_template_for_problem(problem, ROOT),
        title_slug=str(problem["titleSlug"]),
    )
    event = EventStore().record_candidate_ready(
        problem=problem,
        identity=identity,
        language=str(meta["language"]),
        code=code,
        validation=args.validation,
        validation_level=args.level,
    )
    _print_json(event)
    return 0


def _candidate_profile(source: str) -> str | None:
    revisions = re.findall(
        r"(?m)^(?:#|//|--)\s*Revised by:.*?/\s*([\w-]+)\s*$",
        source[:2000],
    )
    if revisions:
        return revisions[-1]
    match = re.search(r"(?m)^(?:#|//|--)\s*Profile:\s*([\w-]+)\s*$", source[:1000])
    if match:
        return match.group(1)
    match = re.search(
        r"(?m)^(?:#|//|--)\s*Completed by:.*?/\s*([\w-]+)\s*$",
        source[:1000],
    )
    return match.group(1) if match else None


def _cmd_backfill_candidates(args: argparse.Namespace) -> int:
    coverage = audit_coverage()
    candidate_hashes = coverage["candidateCodeSha256"]
    catalog = load_catalog()
    by_slug = {str(item["titleSlug"]): item for item in catalog["problems"]}
    configured = {profile.id for profile in load_profiles().profiles}
    store = EventStore()
    events = store.effective_events()
    started_pairs = {
        (str(event["slug"]), str(event["profile_id"]))
        for event in events
        if event.get("type") in {"problem_started", "profile_started"}
        and event.get("slug")
        and event.get("profile_id")
    }
    current_candidates: dict[tuple[str, str], str] = {}
    current_candidate_profiles_by_slug_and_hash: dict[tuple[str, str], str] = {}
    for event in events:
        if (
            event.get("type") == "candidate_ready"
            and event.get("slug")
            and event.get("profile_id")
        ):
            current_candidates[(str(event["slug"]), str(event["profile_id"]))] = str(
                event.get("code_sha256") or ""
            )
            current_candidate_profiles_by_slug_and_hash[
                (str(event["slug"]), str(event.get("code_sha256") or ""))
            ] = str(event["profile_id"])

    appended = 0
    skipped = 0
    failures: list[str] = []
    for slug, code_hash in sorted(candidate_hashes.items()):
        problem = by_slug.get(slug)
        if problem is None:
            failures.append(f"{slug}: catalog entry missing")
            continue
        directory = ROOT / "problems" / problem_key(problem)
        try:
            meta = json.loads((directory / "meta.json").read_text(encoding="utf-8"))
            source = (directory / str(meta["solutionFile"])).read_text(encoding="utf-8")
        except (FileNotFoundError, KeyError, json.JSONDecodeError) as exc:
            failures.append(f"{slug}: {exc}")
            continue
        profile_id = _candidate_profile(source)
        if profile_id is None:
            profile_id = current_candidate_profiles_by_slug_and_hash.get((slug, code_hash))
        pair = (slug, str(profile_id))
        if profile_id not in configured:
            failures.append(f"{slug}: unrecognized Profile in solution header: {profile_id}")
            continue
        if pair not in started_pairs:
            failures.append(f"{slug}: Profile {profile_id} was never started")
            continue
        if current_candidates.get(pair) == code_hash:
            skipped += 1
            continue
        store.append(
            "candidate_ready",
            slug=slug,
            question_id=str(problem.get("questionId") or problem.get("id", "")),
            frontend_id=str(problem.get("questionFrontendId", "")),
            language=str(meta["language"]),
            code_sha256=code_hash,
            validation=args.validation,
            validation_level="static_gate",
            source="backfill-candidates",
            profile_id=profile_id,
            model=next(profile.model for profile in load_profiles().profiles if profile.id == profile_id),
            reasoning_effort=next(
                profile.reasoning_effort
                for profile in load_profiles().profiles
                if profile.id == profile_id
            ),
            client="Codex Desktop",
        )
        appended += 1
    result = {"appended": appended, "skipped": skipped, "failures": failures}
    _print_json(result)
    return 1 if failures else 0


def _cmd_profiles(args: argparse.Namespace) -> int:
    config = load_profiles()
    _print_json(
        {
            "defaultProfile": config.default_profile,
            "executionLadder": list(config.execution_ladder),
            "profiles": [
                {
                    "id": profile.id,
                    "model": profile.model,
                    "reasoningEffort": profile.reasoning_effort,
                    "cohort": profile.cohort,
                    "stage": profile.stage,
                    "enabled": profile.enabled,
                    "description": profile.description,
                }
                for profile in config.profiles
            ],
        }
    )
    return 0


def _cmd_execution_ladder(args: argparse.Namespace) -> int:
    for profile_id in load_profiles().execution_ladder:
        print(profile_id)
    return 0


def _cmd_stats(args: argparse.Namespace) -> int:
    config = load_config()
    summary = write_stats(config.attempt_budget)
    print(
        f"题库 {summary['catalogTotal']}，已归档 {summary['archivedDetails']}，"
        f"已开始 {summary['started']}，Accepted {summary['accepted']}，"
        f"待人工复盘 {summary['reviewRequired']}"
    )
    return 0


def _cmd_quota_status(args: argparse.Namespace) -> int:
    status = submission_quota_status(
        EventStore().effective_events(),
        limit=args.limit,
        window_hours=args.window_hours,
        buffer_seconds=args.buffer_seconds,
        accounting=args.accounting,
    )
    print(json.dumps(status, ensure_ascii=False, separators=(",", ":")))
    return 0


def _cmd_escalation_status(args: argparse.Namespace) -> int:
    summary = build_summary(load_config().attempt_budget)
    items = summary["escalationQueueByProfile"].get(args.profile, [])
    pending = [item for item in items if item["needsNewCandidate"]]
    _print_json(
        {
            "profileId": args.profile,
            "assigned": len(items),
            "candidateReady": len(items) - len(pending),
            "needsNewCandidate": len(pending),
            "pendingSlugs": [item["slug"] for item in pending],
        }
    )
    return 0


def _cmd_audit(args: argparse.Namespace) -> int:
    report = write_coverage()
    _print_json(report)
    return 0 if report["invalidLocalCandidates"] == 0 else 2


def _cmd_status(args: argparse.Namespace) -> int:
    config = load_config()
    if args.selector:
        identity = _identity(args)
        assert identity is not None
        problem = resolve_problem(args.selector)
        usage = EventStore().usage(str(problem["titleSlug"]), identity.profile_id)
        _print_json(
            {
                "frontendId": problem.get("questionFrontendId"),
                "slug": problem.get("titleSlug"),
                "profileId": identity.profile_id,
                "model": identity.model,
                "reasoningEffort": identity.reasoning_effort,
                "round": usage.round_number,
                "remoteTestsThisRound": usage.remote_tests,
                "submissionsThisRound": usage.submissions,
                "accepted": usage.accepted,
                "deferred": usage.deferred,
            }
        )
    else:
        summary = build_summary(config.attempt_budget)
        _print_json(summary)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ai-lc", description="AI LeetCode 刷题实验 CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_profile(argument_parser: argparse.ArgumentParser, *, required: bool = False) -> None:
        argument_parser.add_argument(
            "--profile",
            required=required,
            help="config/profiles.json 中的 Profile ID；覆盖本地默认值",
        )

    doctor = subparsers.add_parser("doctor", help="检查运行时、身份、密钥、题库和登录")
    doctor.add_argument("--offline", action="store_true", help="跳过登录检查")
    add_profile(doctor)
    doctor.set_defaults(func=_cmd_doctor)

    sync = subparsers.add_parser("sync", help="同步题库目录与题面归档")
    sync.add_argument("--with-content", action="store_true", help="同时断点下载全部题面与代码模板")
    sync.add_argument("--refresh", action="store_true", help="重新下载已有题面")
    sync.add_argument("--detail-limit", type=int, help="仅下载指定数量题面（用于联调）")
    sync.set_defaults(func=_cmd_sync)

    next_parser = subparsers.add_parser("next", help="选择下一道未完成题目")
    next_parser.add_argument("--difficulty", choices=["easy", "medium", "hard"])
    next_parser.add_argument("--include-paid", action="store_true")
    next_parser.add_argument(
        "--candidate-ready-only",
        action="store_true",
        help="仅返回当前 Profile 的 candidate-ready 哈希与工作区代码一致的题",
    )
    add_profile(next_parser)
    next_parser.set_defaults(func=_cmd_next)

    start = subparsers.add_parser("start", help="从归档创建本地题目工作目录")
    start.add_argument("selector", help="题号、内部 ID 或 title slug")
    start.add_argument("--language", help="LeetCode langSlug，例如 python3/cpp/rust")
    add_profile(start)
    start.set_defaults(func=_cmd_start)

    test = subparsers.add_parser("test", help="消耗预算执行 LeetCode 远程试跑")
    test.add_argument("selector")
    test.add_argument("--input", help="测试输入；可用 \\n 表示换行")
    test.add_argument("--input-file", help="从 UTF-8 文件读取测试输入")
    add_profile(test)
    test.set_defaults(func=_cmd_test)

    submit = subparsers.add_parser("submit", help="消耗预算正式提交并等待判题")
    submit.add_argument("selector")
    submit.add_argument(
        "--defer-stats",
        action="store_true",
        help="批量提交时暂缓重建统计；整批结束后必须运行 stats",
    )
    submit.add_argument(
        "--account-reconciliation",
        action="store_true",
        help=(
            "仅对 sync 后仍为 ATTEMPTED、且仓库已有 Accepted 与匹配候选哈希的题重提；"
            "计入远程滚动额度但不计入模型实验指标"
        ),
    )
    add_profile(submit)
    submit.set_defaults(func=_cmd_submit)

    retry = subparsers.add_parser("retry", help="第一轮耗尽后开启最终重试轮")
    retry.add_argument("selector")
    retry.add_argument("--reason", required=True, help="至少 10 个字符的新思路说明")
    add_profile(retry)
    retry.set_defaults(func=_cmd_retry)

    defer = subparsers.add_parser("defer", help="在当前 Profile 跳过难题，不阻塞后续选题")
    defer.add_argument("selector")
    defer.add_argument("--reason", required=True, help="当前档位跳过原因")
    add_profile(defer)
    defer.set_defaults(func=_cmd_defer)

    resume = subparsers.add_parser("resume", help="追加事件恢复当前 Profile 的 defer 题")
    resume.add_argument("selector")
    resume.add_argument("--reason", required=True, help="恢复依据，例如已得到可靠本地候选")
    add_profile(resume, required=True)
    resume.set_defaults(func=_cmd_resume)

    annotate = subparsers.add_parser("annotate-profile", help="以追加事件无损校正历史 Profile")
    annotate.add_argument("selector")
    annotate.add_argument("--event-id", action="append", help="可重复指定待校正事件 ID")
    annotate.add_argument("--all-existing", action="store_true", help="校正该题目前的全部事实事件")
    annotate.add_argument("--reason", required=True, help="校正依据")
    add_profile(annotate, required=True)
    annotate.set_defaults(func=_cmd_annotate_profile)

    annotate_result = subparsers.add_parser(
        "annotate-result", help="以追加事件无损校正远程结果分类"
    )
    annotate_result.add_argument("selector")
    annotate_result.add_argument("--event-id", required=True, help="待校正结果事件 ID")
    annotate_result.add_argument(
        "--outcome",
        required=True,
        choices=["infrastructure_error", "failed", "rejected", "accepted"],
    )
    annotate_result.add_argument(
        "--counts-against-budget",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="是否计入模型实验尝试预算",
    )
    annotate_result.add_argument("--classification", required=True)
    annotate_result.add_argument("--reason", required=True)
    annotate_result.set_defaults(func=_cmd_annotate_result)

    report_usage = subparsers.add_parser("report-usage", help="追加客户端提供的精确 Token/耗时数据")
    report_usage.add_argument("selector")
    report_usage.add_argument("--input-tokens", type=int)
    report_usage.add_argument("--output-tokens", type=int)
    report_usage.add_argument("--cached-input-tokens", type=int)
    report_usage.add_argument("--elapsed-seconds", type=float)
    report_usage.add_argument("--source", required=True, help="可核验的数据来源，例如客户端 usage API")
    add_profile(report_usage)
    report_usage.set_defaults(func=_cmd_report_usage)

    candidate_ready = subparsers.add_parser(
        "candidate-ready", help="记录已通过本地验证的候选代码及哈希"
    )
    candidate_ready.add_argument("selector")
    candidate_ready.add_argument("--validation", required=True, help="可核验的本地验证摘要")
    candidate_ready.add_argument(
        "--level",
        choices=["samples", "oracle", "manual"],
        default="oracle",
        help="本地验证层级；默认 oracle",
    )
    add_profile(candidate_ready, required=True)
    candidate_ready.set_defaults(func=_cmd_candidate_ready)

    backfill_candidates = subparsers.add_parser(
        "backfill-candidates", help="按解答署名为全部静态门禁候选补充哈希事件"
    )
    backfill_candidates.add_argument(
        "--validation",
        default="全量覆盖审计：必要文件、语言映射、无占位标记及可用原语言语法门禁通过",
    )
    backfill_candidates.set_defaults(func=_cmd_backfill_candidates)

    profiles = subparsers.add_parser("profiles", help="列出模型与推理档位实验 Profile")
    profiles.set_defaults(func=_cmd_profiles)

    execution_ladder = subparsers.add_parser(
        "execution-ladder", help="逐行列出本实验的 Profile 执行顺序"
    )
    execution_ladder.set_defaults(func=_cmd_execution_ladder)

    stats = subparsers.add_parser("stats", help="重建统计报告")
    stats.set_defaults(func=_cmd_stats)

    quota_status = subparsers.add_parser(
        "quota-status", help="按本地判题证据计算滚动提交额度窗口"
    )
    quota_status.add_argument("--limit", type=int, default=500)
    quota_status.add_argument("--window-hours", type=float, default=24)
    quota_status.add_argument("--buffer-seconds", type=int, default=15)
    quota_status.add_argument(
        "--accounting",
        choices=["remote", "experiment"],
        default="remote",
        help="remote 保护实际请求频率；experiment 按模型尝试预算核算",
    )
    quota_status.set_defaults(func=_cmd_quota_status)

    escalation_status = subparsers.add_parser(
        "escalation-status", help="查看指定 Profile 的升档候选准备状态"
    )
    add_profile(escalation_status, required=True)
    escalation_status.set_defaults(func=_cmd_escalation_status)

    audit = subparsers.add_parser("audit", help="审计全部免费题的本地候选覆盖与静态门禁")
    audit.set_defaults(func=_cmd_audit)

    status = subparsers.add_parser("status", help="查看全局或单题状态")
    status.add_argument("selector", nargs="?")
    add_profile(status)
    status.set_defaults(func=_cmd_status)
    return parser


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="replace")
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (ConfigError, ArchiveError, BudgetError, ApiError, RuntimeError, OSError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
