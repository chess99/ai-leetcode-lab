from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from .archive import load_catalog
from .client import ApiError, LeetCodeClient
from .config import ConfigError, ExperimentConfig, ROOT, load_credentials, load_identity


@dataclass(frozen=True)
class Check:
    name: str
    ok: bool
    detail: str


def _git_ignored(root: Path, relative: str) -> bool:
    result = subprocess.run(
        ["git", "check-ignore", "-q", relative],
        cwd=root,
        check=False,
        capture_output=True,
    )
    return result.returncode == 0


def run_doctor(
    config: ExperimentConfig,
    *,
    offline: bool = False,
    profile_id: str | None = None,
    root: Path = ROOT,
) -> list[Check]:
    checks: list[Check] = []
    checks.append(Check("Python", sys.version_info >= (3, 11), sys.version.split()[0]))
    checks.append(Check("Git 仓库", (root / ".git").exists(), str(root)))
    try:
        identity = load_identity(root, required=config.identity_required, profile_id=profile_id)
        checks.append(
            Check(
                "AI 身份",
                True,
                (
                    f"{identity.client} / {identity.model} / {identity.reasoning_effort} "
                    f"({identity.profile_id})"
                )
                if identity
                else "未要求",
            )
        )
    except ConfigError as exc:
        checks.append(Check("AI 身份", False, str(exc)))

    try:
        credentials = load_credentials(root, required=not offline)
        checks.append(Check("本地凭证", credentials is not None or offline, "已加载（内容不显示）" if credentials else "离线模式"))
    except ConfigError as exc:
        credentials = None
        checks.append(Check("本地凭证", False, str(exc)))

    for relative in (".secrets/leetcode.env", ".ai/identity.env", ".runtime/remote-action.lock"):
        checks.append(Check(f"Git 忽略 {relative}", _git_ignored(root, relative), "已忽略" if _git_ignored(root, relative) else "未忽略"))

    hooks = subprocess.run(
        ["git", "config", "--get", "core.hooksPath"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    ).stdout.strip()
    checks.append(Check("Git 密钥钩子", hooks == ".githooks", hooks or "未配置"))

    try:
        catalog = load_catalog(root)
        checks.append(Check("题库目录", True, f"{catalog.get('total', 0)} 题，{catalog.get('syncedAt', '未知时间')}"))
    except Exception as exc:
        checks.append(Check("题库目录", False, str(exc)))

    if not offline and credentials:
        try:
            status = LeetCodeClient(config, credentials).check_auth()
            checks.append(
                Check(
                    "LeetCode 登录",
                    bool(status.get("isSignedIn")),
                    f"{status.get('username', 'unknown')}，Premium={bool(status.get('isPremium'))}",
                )
            )
        except ApiError as exc:
            checks.append(Check("LeetCode 登录", False, str(exc)))
    elif offline:
        checks.append(Check("LeetCode 登录", True, "离线检查已跳过"))
    return checks


def print_checks(checks: list[Check]) -> bool:
    for check in checks:
        marker = "OK" if check.ok else "FAIL"
        print(f"[{marker}] {check.name}: {check.detail}")
    return all(check.ok for check in checks)
