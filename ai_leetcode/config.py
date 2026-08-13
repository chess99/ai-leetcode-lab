from __future__ import annotations

import json
import os
import re
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent


class ConfigError(RuntimeError):
    """Raised when local configuration is missing or invalid."""


@dataclass(frozen=True)
class AttemptBudget:
    remote_tests_per_round: int
    submissions_per_round: int
    max_rounds: int
    poll_interval_seconds: float
    poll_timeout_seconds: float
    scope: str = "problem_profile"


@dataclass(frozen=True)
class ArchiveConfig:
    page_size: int
    concurrency: int
    request_delay_ms: int


@dataclass(frozen=True)
class ExperimentConfig:
    endpoint: str
    default_language: str
    archive: ArchiveConfig
    attempt_budget: AttemptBudget
    identity_required: bool


@dataclass(frozen=True)
class Credentials:
    csrf_token: str
    session: str

    @property
    def cookie_header(self) -> str:
        return f"csrftoken={self.csrf_token}; LEETCODE_SESSION={self.session}"


@dataclass(frozen=True)
class Identity:
    client: str
    model: str
    reasoning_effort: str = "unspecified"
    profile_id: str = "unprofiled"


@dataclass(frozen=True)
class Profile:
    id: str
    model: str
    reasoning_effort: str
    cohort: str
    stage: int
    enabled: bool
    description: str


@dataclass(frozen=True)
class ProfilesConfig:
    default_profile: str
    profiles: tuple[Profile, ...]
    execution_ladder: tuple[str, ...] = ()

    def get(self, profile_id: str) -> Profile:
        for profile in self.profiles:
            if profile.id == profile_id:
                return profile
        raise ConfigError(f"未知实验 Profile：{profile_id}")


LANGUAGE_EXTENSIONS = {
    "bash": "sh",
    "c": "c",
    "cpp": "cpp",
    "csharp": "cs",
    "dart": "dart",
    "elixir": "ex",
    "erlang": "erl",
    "golang": "go",
    "java": "java",
    "javascript": "js",
    "kotlin": "kt",
    "mysql": "sql",
    "mssql": "sql",
    "oraclesql": "sql",
    "php": "php",
    "python": "py",
    "python3": "py",
    "racket": "rkt",
    "ruby": "rb",
    "rust": "rs",
    "scala": "scala",
    "swift": "swift",
    "typescript": "ts",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigError(f"缺少配置文件：{path}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigError(f"JSON 格式错误：{path}: {exc}") from exc


def load_config(root: Path = ROOT) -> ExperimentConfig:
    raw = load_json(root / "config" / "experiment.json")
    archive = raw.get("archive", {})
    budget = raw.get("attempt_budget", {})
    config = ExperimentConfig(
        endpoint=str(raw.get("endpoint", "https://leetcode.cn")).rstrip("/"),
        default_language=str(raw.get("default_language", "python3")),
        archive=ArchiveConfig(
            page_size=int(archive.get("page_size", 100)),
            concurrency=int(archive.get("concurrency", 4)),
            request_delay_ms=int(archive.get("request_delay_ms", 200)),
        ),
        attempt_budget=AttemptBudget(
            remote_tests_per_round=int(budget.get("remote_tests_per_round", 5)),
            submissions_per_round=int(budget.get("submissions_per_round", 3)),
            max_rounds=int(budget.get("max_rounds", 2)),
            poll_interval_seconds=float(budget.get("poll_interval_seconds", 1.5)),
            poll_timeout_seconds=float(budget.get("poll_timeout_seconds", 120)),
            scope=str(budget.get("scope", "problem_profile")),
        ),
        identity_required=bool(raw.get("identity_required", True)),
    )
    if config.archive.page_size < 1 or config.archive.concurrency < 1:
        raise ConfigError("归档 page_size 和 concurrency 必须大于 0")
    if min(
        config.attempt_budget.remote_tests_per_round,
        config.attempt_budget.submissions_per_round,
        config.attempt_budget.max_rounds,
    ) < 1:
        raise ConfigError("尝试预算必须大于 0")
    if config.attempt_budget.scope != "problem_profile":
        raise ConfigError("attempt_budget.scope 目前只支持 problem_profile")
    return config


def load_profiles(root: Path = ROOT) -> ProfilesConfig:
    raw = load_json(root / "config" / "profiles.json")
    raw_profiles = raw.get("profiles")
    if not isinstance(raw_profiles, list) or not raw_profiles:
        raise ConfigError("config/profiles.json 至少需要一个 Profile")
    allowed_efforts = {"low", "medium", "high", "xhigh", "max", "ultra"}
    profiles: list[Profile] = []
    seen: set[str] = set()
    for raw_profile in raw_profiles:
        if not isinstance(raw_profile, dict):
            raise ConfigError("Profile 配置必须是 JSON 对象")
        profile_id = str(raw_profile.get("id", "")).strip()
        model = str(raw_profile.get("model", "")).strip()
        reasoning_effort = str(raw_profile.get("reasoningEffort", "")).strip().lower()
        if not profile_id or profile_id in seen:
            raise ConfigError(f"Profile ID 为空或重复：{profile_id or '<empty>'}")
        if not model:
            raise ConfigError(f"Profile {profile_id} 缺少 model")
        if reasoning_effort not in allowed_efforts:
            raise ConfigError(
                f"Profile {profile_id} 的 reasoningEffort 必须是 "
                f"{', '.join(sorted(allowed_efforts))} 之一"
            )
        seen.add(profile_id)
        profiles.append(
            Profile(
                id=profile_id,
                model=model,
                reasoning_effort=reasoning_effort,
                cohort=str(raw_profile.get("cohort", "unspecified")).strip() or "unspecified",
                stage=int(raw_profile.get("stage", 0)),
                enabled=bool(raw_profile.get("enabled", True)),
                description=str(raw_profile.get("description", "")).strip(),
            )
        )
    default_profile = str(raw.get("defaultProfile", "")).strip()
    if default_profile not in seen:
        raise ConfigError(f"defaultProfile 不存在：{default_profile}")
    raw_ladder = raw.get("executionLadder", [])
    if not isinstance(raw_ladder, list):
        raise ConfigError("executionLadder 必须是 Profile ID 数组")
    execution_ladder = tuple(str(profile_id).strip() for profile_id in raw_ladder)
    if any(not profile_id or profile_id not in seen for profile_id in execution_ladder):
        raise ConfigError("executionLadder 包含空值或未知 Profile")
    if len(set(execution_ladder)) != len(execution_ladder):
        raise ConfigError("executionLadder 不允许重复 Profile")
    disabled = {
        profile.id for profile in profiles if not profile.enabled
    } & set(execution_ladder)
    if disabled:
        raise ConfigError(
            f"executionLadder 包含未启用 Profile：{', '.join(sorted(disabled))}"
        )
    return ProfilesConfig(
        default_profile=default_profile,
        profiles=tuple(profiles),
        execution_ladder=execution_ladder,
    )


def read_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except FileNotFoundError:
        return values
    for number, raw_line in enumerate(lines, 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise ConfigError(f"环境文件格式错误：{path}:{number}")
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def load_credentials(root: Path = ROOT, required: bool = True) -> Credentials | None:
    local = read_env_file(root / ".secrets" / "leetcode.env")
    csrf = os.environ.get("LEETCODE_CSRF_TOKEN") or local.get("LEETCODE_CSRF_TOKEN", "")
    session = os.environ.get("LEETCODE_SESSION") or local.get("LEETCODE_SESSION", "")
    if not csrf or not session:
        if required:
            raise ConfigError(
                "缺少 LeetCode 凭证；请填写 .secrets/leetcode.env 中的 "
                "LEETCODE_CSRF_TOKEN 与 LEETCODE_SESSION"
            )
        return None
    return Credentials(csrf_token=csrf, session=session)


def load_identity(
    root: Path = ROOT,
    required: bool = True,
    profile_id: str | None = None,
) -> Identity | None:
    local = read_env_file(root / ".ai" / "identity.env")
    client = os.environ.get("AI_CLIENT_NAME") or local.get("AI_CLIENT_NAME", "")
    selected_profile = profile_id or os.environ.get("AI_PROFILE_ID") or local.get("AI_PROFILE_ID", "")
    selected_profile = selected_profile.strip()
    if selected_profile:
        profile = load_profiles(root).get(selected_profile)
        model = profile.model
        reasoning_effort = profile.reasoning_effort
    else:
        model = os.environ.get("AI_MODEL_NAME") or local.get("AI_MODEL_NAME", "")
        reasoning_effort = (
            os.environ.get("AI_REASONING_EFFORT")
            or local.get("AI_REASONING_EFFORT", "unspecified")
        ).strip().lower()
        selected_profile = "unprofiled"
    placeholders = {"your-ai-client", "your-model", "unknown", ""}
    if client.strip().lower() in placeholders or model.strip().lower() in placeholders:
        if required:
            raise ConfigError(
                "缺少 AI 身份；请在 .ai/identity.env 填写 AI_CLIENT_NAME，并配置 "
                "AI_PROFILE_ID（推荐）或 AI_MODEL_NAME"
            )
        return None
    return Identity(
        client=client.strip(),
        model=model.strip(),
        reasoning_effort=reasoning_effort,
        profile_id=selected_profile,
    )


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        os.replace(temp_path, path)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n")


def safe_component(value: str) -> str:
    cleaned = re.sub(r"[^0-9A-Za-z._-]+", "-", value.strip())
    return cleaned.strip("-._") or "unknown"


def display_id(value: str | int) -> str:
    text = str(value)
    return text.zfill(4) if text.isdigit() else safe_component(text)


def problem_key(problem: dict[str, Any]) -> str:
    return f"{display_id(problem.get('questionFrontendId', problem.get('id', 'unknown')))}-{safe_component(str(problem['titleSlug']))}"
