from __future__ import annotations

import argparse
import json
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
from .config import ConfigError, ROOT, load_config, load_credentials, load_identity
from .doctor import print_checks, run_doctor
from .events import BudgetError, EventStore
from .runner import RemoteActionLock, run_remote_test, submit_solution
from .stats import build_summary, write_stats


def _client(config: Any, *, credentials_required: bool) -> LeetCodeClient:
    credentials = load_credentials(ROOT, required=credentials_required)
    return LeetCodeClient(config, credentials)


def _print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def _cmd_doctor(args: argparse.Namespace) -> int:
    config = load_config()
    return 0 if print_checks(run_doctor(config, offline=args.offline)) else 1


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
    catalog = load_catalog()
    store = EventStore()
    events = store.load()
    started = {event.get("slug") for event in events if event.get("type") == "problem_started"}
    accepted = {
        event.get("slug")
        for event in events
        if event.get("type") == "submission_result" and event.get("outcome") == "accepted"
    }
    active = [
        item
        for item in catalog["problems"]
        if item["titleSlug"] in started - accepted and _eligible(item, args.difficulty, args.include_paid)
    ]
    candidates = active or [
        item
        for item in catalog["problems"]
        if item["titleSlug"] not in started and _eligible(item, args.difficulty, args.include_paid)
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
    identity = load_identity(required=config.identity_required)
    assert identity is not None
    problem = resolve_problem(args.selector)
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
        EventStore(),
        language=args.language or config.default_language,
    )
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
    identity = load_identity(required=True)
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
    identity = load_identity(required=True)
    assert identity is not None
    result = submit_solution(
        args.selector,
        _client(config, credentials_required=True),
        config,
        identity,
        EventStore(),
    )
    _print_json(result)
    write_stats(config.attempt_budget)
    return 0 if result.get("outcome") == "accepted" else 2


def _cmd_retry(args: argparse.Namespace) -> int:
    config = load_config()
    identity = load_identity(required=True)
    assert identity is not None
    problem = resolve_problem(args.selector)
    with RemoteActionLock():
        event = EventStore().open_retry(str(problem["titleSlug"]), args.reason, config.attempt_budget, identity)
    _print_json(event)
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


def _cmd_status(args: argparse.Namespace) -> int:
    config = load_config()
    if args.selector:
        problem = resolve_problem(args.selector)
        usage = EventStore().usage(str(problem["titleSlug"]))
        _print_json(
            {
                "frontendId": problem.get("questionFrontendId"),
                "slug": problem.get("titleSlug"),
                "round": usage.round_number,
                "remoteTestsThisRound": usage.remote_tests,
                "submissionsThisRound": usage.submissions,
                "accepted": usage.accepted,
            }
        )
    else:
        summary = build_summary(config.attempt_budget)
        _print_json(summary)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ai-lc", description="AI LeetCode 刷题实验 CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser("doctor", help="检查运行时、身份、密钥、题库和登录")
    doctor.add_argument("--offline", action="store_true", help="跳过登录检查")
    doctor.set_defaults(func=_cmd_doctor)

    sync = subparsers.add_parser("sync", help="同步题库目录与题面归档")
    sync.add_argument("--with-content", action="store_true", help="同时断点下载全部题面与代码模板")
    sync.add_argument("--refresh", action="store_true", help="重新下载已有题面")
    sync.add_argument("--detail-limit", type=int, help="仅下载指定数量题面（用于联调）")
    sync.set_defaults(func=_cmd_sync)

    next_parser = subparsers.add_parser("next", help="选择下一道未完成题目")
    next_parser.add_argument("--difficulty", choices=["easy", "medium", "hard"])
    next_parser.add_argument("--include-paid", action="store_true")
    next_parser.set_defaults(func=_cmd_next)

    start = subparsers.add_parser("start", help="从归档创建本地题目工作目录")
    start.add_argument("selector", help="题号、内部 ID 或 title slug")
    start.add_argument("--language", help="LeetCode langSlug，例如 python3/cpp/rust")
    start.set_defaults(func=_cmd_start)

    test = subparsers.add_parser("test", help="消耗预算执行 LeetCode 远程试跑")
    test.add_argument("selector")
    test.add_argument("--input", help="测试输入；可用 \\n 表示换行")
    test.add_argument("--input-file", help="从 UTF-8 文件读取测试输入")
    test.set_defaults(func=_cmd_test)

    submit = subparsers.add_parser("submit", help="消耗预算正式提交并等待判题")
    submit.add_argument("selector")
    submit.set_defaults(func=_cmd_submit)

    retry = subparsers.add_parser("retry", help="第一轮耗尽后开启最终重试轮")
    retry.add_argument("selector")
    retry.add_argument("--reason", required=True, help="至少 10 个字符的新思路说明")
    retry.set_defaults(func=_cmd_retry)

    stats = subparsers.add_parser("stats", help="重建统计报告")
    stats.set_defaults(func=_cmd_stats)

    status = subparsers.add_parser("status", help="查看全局或单题状态")
    status.add_argument("selector", nargs="?")
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
