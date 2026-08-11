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
    return config


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


def load_identity(root: Path = ROOT, required: bool = True) -> Identity | None:
    local = read_env_file(root / ".ai" / "identity.env")
    client = os.environ.get("AI_CLIENT_NAME") or local.get("AI_CLIENT_NAME", "")
    model = os.environ.get("AI_MODEL_NAME") or local.get("AI_MODEL_NAME", "")
    placeholders = {"your-ai-client", "your-model", "unknown", ""}
    if client.strip().lower() in placeholders or model.strip().lower() in placeholders:
        if required:
            raise ConfigError(
                "缺少 AI 身份；请在 .ai/identity.env 填写当前 AI_CLIENT_NAME 与 AI_MODEL_NAME"
            )
        return None
    return Identity(client=client.strip(), model=model.strip())


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
