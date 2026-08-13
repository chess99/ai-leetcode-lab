from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Iterable


def _parse_utc(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def submission_quota_status(
    events: Iterable[dict[str, Any]],
    *,
    limit: int = 500,
    window_hours: float = 24,
    buffer_seconds: int = 15,
    now: datetime | None = None,
) -> dict[str, Any]:
    """Return a conservative rolling-window gate for formal submissions.

    Only judge responses that count against the experiment budget consume a
    slot. An unfinished request is counted conservatively, while explicit
    infrastructure failures such as HTTP 429 are not.
    """
    if limit <= 0:
        raise ValueError("limit must be positive")
    if window_hours <= 0:
        raise ValueError("window_hours must be positive")
    if buffer_seconds < 0:
        raise ValueError("buffer_seconds cannot be negative")

    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    window = timedelta(hours=window_hours)
    starts: dict[str, datetime] = {}
    results: dict[str, dict[str, Any]] = {}
    for event in events:
        action_id = str(event.get("action_id") or "")
        if not action_id:
            continue
        if event.get("type") == "submission_started" and event.get("timestamp"):
            starts[action_id] = _parse_utc(str(event["timestamp"]))
        elif event.get("type") == "submission_result":
            results[action_id] = event

    charged: list[datetime] = []
    for action_id, started_at in starts.items():
        result = results.get(action_id)
        if result is not None and not bool(result.get("counts_against_budget", True)):
            continue
        if current - window < started_at <= current:
            charged.append(started_at)
    charged.sort()

    wait_seconds = 0
    next_allowed_at = None
    if len(charged) >= limit:
        # The (count-limit)-th oldest charged request must leave the window
        # before another request can be sent.
        release = charged[len(charged) - limit] + window + timedelta(seconds=buffer_seconds)
        wait_seconds = max(0, int((release - current).total_seconds() + 0.999999))
        next_allowed_at = release.isoformat().replace("+00:00", "Z")

    return {
        "schemaVersion": 1,
        "limit": limit,
        "windowHours": window_hours,
        "bufferSeconds": buffer_seconds,
        "used": len(charged),
        "remaining": max(0, limit - len(charged)),
        "waitSeconds": wait_seconds,
        "nextAllowedAt": next_allowed_at,
        "policy": "rolling_window_local_evidence",
    }
