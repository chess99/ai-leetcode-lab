from __future__ import annotations

from collections import Counter
from datetime import datetime
import hashlib
import json
from pathlib import Path
from statistics import mean, median
from typing import Any

from .archive import load_catalog
from .config import (
    AttemptBudget,
    ROOT,
    atomic_write_json,
    atomic_write_text,
    load_profiles,
    problem_key,
    utc_now,
)
from .events import EventStore


def _timestamp(value: Any) -> datetime | None:
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def _event_profile(
    event: dict[str, Any],
    starts_by_action: dict[Any, dict[str, Any]],
) -> str:
    if event.get("profile_id"):
        return str(event["profile_id"])
    start = starts_by_action.get(event.get("action_id"), {})
    return str(start.get("profile_id") or "unprofiled")


def build_summary(budget: AttemptBudget, *, root: Path = ROOT) -> dict[str, Any]:
    catalog = load_catalog(root)
    problems = catalog["problems"]
    by_slug = {str(item["titleSlug"]): item for item in problems}
    store = EventStore(root)
    events = store.effective_events()
    configured_profiles = load_profiles(root)
    profile_config = {profile.id: profile for profile in configured_profiles.profiles}

    started = {
        str(event["slug"])
        for event in events
        if event.get("type") == "problem_started" and event.get("slug")
    }
    profile_starts = [
        event
        for event in events
        if event.get("type") in {"problem_started", "profile_started"}
        and event.get("slug")
        and event.get("profile_id")
    ]
    started_pairs = {
        (str(event["slug"]), str(event["profile_id"])) for event in profile_starts
    }
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
    submission_starts_by_action = {event.get("action_id"): event for event in submission_starts}
    test_starts = [event for event in events if event.get("type") == "remote_test_started"]
    action_starts_by_action = {
        event.get("action_id"): event for event in [*test_starts, *submission_starts]
    }
    result_events = [
        event
        for event in events
        if event.get("type") in {"remote_test_result", "submission_result"}
    ]
    results_by_action = {event.get("action_id"): event for event in result_events}
    infrastructure_result_events = [
        event for event in result_events if event.get("outcome") == "infrastructure_error"
    ]

    def charged_starts(starts: list[dict[str, Any]]) -> list[dict[str, Any]]:
        charged: list[dict[str, Any]] = []
        for start in starts:
            result = results_by_action.get(start.get("action_id"))
            if result is None or result.get("counts_against_budget", True):
                charged.append(start)
        return charged

    charged_submission_starts = charged_starts(submission_starts)
    charged_test_starts = charged_starts(test_starts)
    deferred_pairs: set[tuple[str, str]] = set()
    for event in events:
        if not event.get("slug") or not event.get("profile_id"):
            continue
        pair = (str(event["slug"]), str(event["profile_id"]))
        if event.get("type") == "profile_deferred":
            deferred_pairs.add(pair)
        elif event.get("type") == "profile_resumed":
            deferred_pairs.discard(pair)

    retry_counts: Counter[tuple[str, str]] = Counter(
        (str(event["slug"]), str(event["profile_id"]))
        for event in events
        if event.get("type") == "retry_opened"
        and event.get("slug")
        and event.get("profile_id")
    )
    charged_submissions_by_pair_and_round: Counter[tuple[str, str, int]] = Counter(
        (
            str(event.get("slug")),
            str(event.get("profile_id")),
            int(event.get("round", 1)),
        )
        for event in charged_submission_starts
        if event.get("slug") and event.get("profile_id")
    )

    first_success_profile: dict[str, str] = {
        slug: _event_profile(event, submission_starts_by_action)
        for slug, event in accepted_by_slug.items()
    }
    first_success_by_problem: dict[str, dict[str, Any]] = {}
    for slug, profile_id in first_success_profile.items():
        problem = by_slug.get(slug, {})
        profile = profile_config.get(profile_id)
        accepted_event = accepted_by_slug[slug]
        identity_event = accepted_event
        if not accepted_event.get("model"):
            identity_event = submission_starts_by_action.get(
                accepted_event.get("action_id"), accepted_event
            )
        first_success_by_problem[slug] = {
            "frontendId": problem.get("questionFrontendId"),
            "difficulty": problem.get("difficulty", "UNKNOWN"),
            "profileId": profile_id,
            "model": identity_event.get("model") or (profile.model if profile else "unknown"),
            "reasoningEffort": (
                identity_event.get("reasoning_effort")
                or (profile.reasoning_effort if profile else "unknown")
            ),
        }
    accepted_by_profile = Counter(first_success_profile.values())
    accepted_by_agent: Counter[str] = Counter()
    for event in accepted_by_slug.values():
        identity_event = event
        if not event.get("client") or not event.get("model"):
            identity_event = submission_starts_by_action.get(event.get("action_id"), event)
        accepted_by_agent[
            f"{identity_event.get('client', 'unknown')} / {identity_event.get('model', 'unknown')}"
        ] += 1

    review_required_pairs: set[tuple[str, str]] = set()
    for slug, profile_id in started_pairs - deferred_pairs:
        if slug in accepted:
            continue
        round_number = 1 + retry_counts[(slug, profile_id)]
        submissions = charged_submissions_by_pair_and_round[
            (slug, profile_id, round_number)
        ]
        if round_number >= budget.max_rounds and submissions >= budget.submissions_per_round:
            review_required_pairs.add((slug, profile_id))

    accessible_problems = [item for item in problems if not item.get("paidOnly")]
    paid_problems = [item for item in problems if item.get("paidOnly")]
    difficulty_total = Counter(
        str(item.get("difficulty", "UNKNOWN")) for item in accessible_problems
    )
    all_difficulty_total = Counter(str(item.get("difficulty", "UNKNOWN")) for item in problems)
    paid_difficulty_total = Counter(str(item.get("difficulty", "UNKNOWN")) for item in paid_problems)
    difficulty_accepted = Counter(
        str(by_slug[slug].get("difficulty", "UNKNOWN")) for slug in accepted if slug in by_slug
    )
    first_success_by_difficulty: dict[str, Counter[str]] = {
        level: Counter() for level in difficulty_total
    }
    for slug, profile_id in first_success_profile.items():
        if slug in by_slug:
            level = str(by_slug[slug].get("difficulty", "UNKNOWN"))
            first_success_by_difficulty.setdefault(level, Counter())[profile_id] += 1

    observed_profiles = {
        str(event["profile_id"])
        for event in events
        if event.get("profile_id") and event.get("type") != "profile_annotation"
    }
    profile_ids = [profile.id for profile in configured_profiles.profiles]
    profile_ids.extend(sorted(observed_profiles - set(profile_ids)))
    usage_reports = [event for event in events if event.get("type") == "usage_reported"]
    candidate_events = [event for event in events if event.get("type") == "candidate_ready"]
    latest_candidate_by_pair: dict[tuple[str, str], dict[str, Any]] = {}
    for event in candidate_events:
        if event.get("slug") and event.get("profile_id"):
            latest_candidate_by_pair[(str(event["slug"]), str(event["profile_id"]))] = event
    profile_stats: dict[str, dict[str, Any]] = {}
    for profile_id in profile_ids:
        profile = profile_config.get(profile_id)
        profile_started_slugs = {slug for slug, pid in started_pairs if pid == profile_id}
        profile_accepted_slugs = {
            slug for slug, pid in first_success_profile.items() if pid == profile_id
        }
        profile_deferred_slugs = {slug for slug, pid in deferred_pairs if pid == profile_id}
        profile_tests = [
            event for event in charged_test_starts if str(event.get("profile_id")) == profile_id
        ]
        profile_submissions = [
            event
            for event in charged_submission_starts
            if str(event.get("profile_id")) == profile_id
        ]
        profile_results = [
            event
            for event in result_events
            if _event_profile(event, action_starts_by_action) == profile_id
        ]
        profile_infrastructure_results = [
            event
            for event in profile_results
            if event.get("outcome") == "infrastructure_error"
        ]
        profile_failed_results = [
            event
            for event in profile_results
            if event.get("type") == "submission_result"
            and event.get("outcome") in {"failed", "rejected"}
            and event.get("counts_against_budget", True)
        ]
        profile_failed_slugs = {
            str(event["slug"]) for event in profile_failed_results if event.get("slug")
        }
        profile_usage_reports = [
            event for event in usage_reports if str(event.get("profile_id")) == profile_id
        ]
        profile_candidate_slugs = {
            slug for slug, pid in latest_candidate_by_pair if pid == profile_id
        }
        remote_elapsed_values = [
            int(event["remote_elapsed_ms"])
            for event in profile_results
            if event.get("remote_elapsed_ms") is not None
        ]
        reported_slugs = {str(event["slug"]) for event in profile_usage_reports if event.get("slug")}

        start_times: dict[str, datetime] = {}
        for event in profile_starts:
            if str(event.get("profile_id")) != profile_id:
                continue
            timestamp = _timestamp(event.get("timestamp"))
            slug = str(event["slug"])
            if timestamp is not None and (slug not in start_times or timestamp < start_times[slug]):
                start_times[slug] = timestamp
        solve_seconds: list[float] = []
        for slug in profile_accepted_slugs:
            accepted_at = _timestamp(accepted_by_slug[slug].get("timestamp"))
            started_at = start_times.get(slug)
            if accepted_at is not None and started_at is not None and accepted_at >= started_at:
                solve_seconds.append((accepted_at - started_at).total_seconds())

        token_totals = {
            "inputTokens": sum(int(event.get("input_tokens", 0)) for event in profile_usage_reports),
            "outputTokens": sum(int(event.get("output_tokens", 0)) for event in profile_usage_reports),
            "cachedInputTokens": sum(
                int(event.get("cached_input_tokens", 0)) for event in profile_usage_reports
            ),
            "elapsedSeconds": sum(
                float(event.get("elapsed_seconds", 0.0)) for event in profile_usage_reports
            ),
        }
        by_difficulty: dict[str, dict[str, int]] = {}
        for level in sorted(difficulty_total):
            by_difficulty[level] = {
                "started": sum(
                    1
                    for slug in profile_started_slugs
                    if str(by_slug.get(slug, {}).get("difficulty", "UNKNOWN")) == level
                ),
                "accepted": sum(
                    1
                    for slug in profile_accepted_slugs
                    if str(by_slug.get(slug, {}).get("difficulty", "UNKNOWN")) == level
                ),
                "deferred": sum(
                    1
                    for slug in profile_deferred_slugs
                    if str(by_slug.get(slug, {}).get("difficulty", "UNKNOWN")) == level
                ),
                "failedSubmissionAttempts": sum(
                    1
                    for event in profile_failed_results
                    if str(
                        by_slug.get(str(event.get("slug")), {}).get(
                            "difficulty", "UNKNOWN"
                        )
                    )
                    == level
                ),
                "failedSubmissionProblems": sum(
                    1
                    for slug in profile_failed_slugs
                    if str(by_slug.get(slug, {}).get("difficulty", "UNKNOWN")) == level
                ),
            }
        profile_stats[profile_id] = {
            "model": profile.model if profile else "unknown",
            "reasoningEffort": profile.reasoning_effort if profile else "unknown",
            "cohort": profile.cohort if profile else "unconfigured",
            "stage": profile.stage if profile else None,
            "enabled": profile.enabled if profile else True,
            "started": len(profile_started_slugs),
            "accepted": len(profile_accepted_slugs),
            "deferred": len(profile_deferred_slugs),
            "candidateReady": len(profile_candidate_slugs),
            "reviewRequired": sum(1 for _, pid in review_required_pairs if pid == profile_id),
            "remoteTests": len(profile_tests),
            "submissions": len(profile_submissions),
            "failedSubmissions": len(profile_failed_results),
            "failedSubmissionProblems": len(profile_failed_slugs),
            "infrastructureErrors": {
                "remoteTests": sum(
                    1
                    for event in profile_infrastructure_results
                    if event.get("type") == "remote_test_result"
                ),
                "submissions": sum(
                    1
                    for event in profile_infrastructure_results
                    if event.get("type") == "submission_result"
                ),
            },
            "firstSubmissionAccepted": sum(
                1
                for slug in profile_accepted_slugs
                if int(accepted_by_slug[slug].get("round", 0)) == 1
                and int(accepted_by_slug[slug].get("attempt", 0)) == 1
            ),
            "remoteElapsedReports": len(remote_elapsed_values),
            "remoteElapsedSeconds": (
                sum(remote_elapsed_values) / 1000 if remote_elapsed_values else None
            ),
            "averageSolveWallSeconds": mean(solve_seconds) if solve_seconds else None,
            "medianSolveWallSeconds": median(solve_seconds) if solve_seconds else None,
            "byDifficulty": by_difficulty,
            "usage": {
                "reports": len(profile_usage_reports),
                "coveredProblems": len(reported_slugs),
                "coverageOfStarted": (
                    len(reported_slugs & profile_started_slugs) / len(profile_started_slugs)
                    if profile_started_slugs
                    else 0.0
                ),
                **token_totals,
            },
        }

    escalation_queue: dict[str, list[dict[str, Any]]] = {profile_id: [] for profile_id in profile_ids}
    profiles_by_cohort: dict[str, list[Any]] = {}
    for profile in configured_profiles.profiles:
        profiles_by_cohort.setdefault(profile.cohort, []).append(profile)
    next_profile: dict[str, str] = {}
    if configured_profiles.execution_ladder:
        next_profile.update(
            zip(
                configured_profiles.execution_ladder,
                configured_profiles.execution_ladder[1:],
            )
        )
    else:
        for cohort_profiles in profiles_by_cohort.values():
            ordered = sorted(
                (profile for profile in cohort_profiles if profile.enabled),
                key=lambda profile: profile.stage,
            )
            for current, following in zip(ordered, ordered[1:]):
                next_profile[current.id] = following.id
    for slug, profile_id in sorted(deferred_pairs):
        target = next_profile.get(profile_id)
        if not target or slug in accepted:
            continue
        if (slug, target) in deferred_pairs:
            # The problem already passed through this target Profile; its current
            # escalation state belongs to a later stage, not this historical edge.
            continue
        target_candidate = latest_candidate_by_pair.get((slug, target))
        escalation_queue.setdefault(target, []).append(
            {
                "slug": slug,
                "fromProfile": profile_id,
                "targetStarted": (slug, target) in started_pairs,
                "targetCandidateReady": target_candidate is not None,
                "needsNewCandidate": target_candidate is None,
            }
        )
    if configured_profiles.execution_ladder:
        ladder_cohorts = {
            profile_config[profile_id].cohort
            for profile_id in configured_profiles.execution_ladder
        }
        highest_profiles = {configured_profiles.execution_ladder[-1]}
        highest_profiles.update(
            max(
                (profile for profile in profiles if profile.enabled),
                key=lambda profile: profile.stage,
            ).id
            for cohort, profiles in profiles_by_cohort.items()
            if cohort not in ladder_cohorts and any(profile.enabled for profile in profiles)
        )
    else:
        highest_profiles = {
            max(
                (profile for profile in profiles if profile.enabled),
                key=lambda profile: profile.stage,
            ).id
            for profiles in profiles_by_cohort.values()
            if any(profile.enabled for profile in profiles)
        }
    unresolved_at_highest = [
        {"profileId": profile_id, "slug": slug}
        for slug, profile_id in sorted(deferred_pairs, key=lambda pair: (pair[1], pair[0]))
        if profile_id in highest_profiles and slug not in accepted
    ]

    first_submission_accepts = sum(
        1
        for event in accepted_by_slug.values()
        if int(event.get("round", 0)) == 1 and int(event.get("attempt", 0)) == 1
    )
    first_round_accepts = sum(
        1 for event in accepted_by_slug.values() if int(event.get("round", 0)) == 1
    )
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
    accessible = len(accessible_problems)
    accessible_accepted = sum(
        1 for slug in accepted if slug in by_slug and not by_slug[slug].get("paidOnly")
    )
    accepted_count = len(accepted)
    reported_pairs = {
        (str(event.get("slug")), str(event.get("profile_id"))) for event in usage_reports
    }
    submitted_slugs = {
        str(event["slug"]) for event in charged_submission_starts if event.get("slug")
    }
    failed_result_events = [
        event
        for event in result_events
        if event.get("type") == "submission_result"
        and event.get("outcome") in {"failed", "rejected"}
        and event.get("counts_against_budget", True)
    ]
    failed_submission_slugs = {
        str(event["slug"]) for event in failed_result_events if event.get("slug")
    }
    awaiting_remote_accepted = {
        str(item["titleSlug"])
        for item in accessible_problems
        if str(item["titleSlug"]) not in accepted
    }

    accepted_code_drift: list[dict[str, Any]] = []
    for slug, accepted_event in accepted_by_slug.items():
        start = submission_starts_by_action.get(accepted_event.get("action_id"), {})
        accepted_hash = str(
            accepted_event.get("code_sha256") or start.get("code_sha256") or ""
        )
        problem = by_slug.get(slug)
        if not accepted_hash or problem is None:
            continue
        directory = root / "problems" / problem_key(problem)
        try:
            meta = json.loads((directory / "meta.json").read_text(encoding="utf-8"))
            current = (directory / str(meta["solutionFile"])).read_text(encoding="utf-8")
        except (FileNotFoundError, KeyError, OSError, UnicodeError, json.JSONDecodeError):
            continue
        current_hash = hashlib.sha256(current.encode("utf-8")).hexdigest()
        if current_hash != accepted_hash:
            latest_candidate = latest_candidate_by_pair.get(
                (slug, _event_profile(accepted_event, submission_starts_by_action))
            )
            drift = {
                "slug": slug,
                "acceptedCodeSha256": accepted_hash,
                "currentCodeSha256": current_hash,
                "currentCandidateRecorded": bool(
                    latest_candidate
                    and str(latest_candidate.get("code_sha256") or "") == current_hash
                ),
            }
            if latest_candidate is not None:
                drift["currentCandidateCodeSha256"] = str(
                    latest_candidate.get("code_sha256") or ""
                )
            accepted_code_drift.append(drift)

    accepted_code_exact_match_count = 0
    for slug, accepted_event in accepted_by_slug.items():
        start = submission_starts_by_action.get(accepted_event.get("action_id"), {})
        accepted_hash = str(
            accepted_event.get("code_sha256") or start.get("code_sha256") or ""
        )
        problem = by_slug.get(slug)
        if not accepted_hash or problem is None:
            continue
        directory = root / "problems" / problem_key(problem)
        try:
            meta = json.loads((directory / "meta.json").read_text(encoding="utf-8"))
            current = (directory / str(meta["solutionFile"])).read_text(encoding="utf-8")
        except (FileNotFoundError, KeyError, OSError, UnicodeError, json.JSONDecodeError):
            continue
        if hashlib.sha256(current.encode("utf-8")).hexdigest() == accepted_hash:
            accepted_code_exact_match_count += 1

    current_candidate_drift: list[dict[str, Any]] = []
    for (slug, profile_id), candidate_event in latest_candidate_by_pair.items():
        candidate_hash = str(candidate_event.get("code_sha256") or "")
        problem = by_slug.get(slug)
        if not candidate_hash or problem is None:
            continue
        directory = root / "problems" / problem_key(problem)
        try:
            meta = json.loads((directory / "meta.json").read_text(encoding="utf-8"))
            current = (directory / str(meta["solutionFile"])).read_text(encoding="utf-8")
        except (FileNotFoundError, KeyError, OSError, UnicodeError, json.JSONDecodeError):
            continue
        current_hash = hashlib.sha256(current.encode("utf-8")).hexdigest()
        if current_hash != candidate_hash:
            current_candidate_drift.append(
                {
                    "slug": slug,
                    "profileId": profile_id,
                    "candidateCodeSha256": candidate_hash,
                    "currentCodeSha256": current_hash,
                }
            )

    ladder_paths: dict[str, list[dict[str, Any]]] = {}
    for slug in sorted(
        {slug for slug, _ in started_pairs}
        | {slug for slug, _ in deferred_pairs}
        | set(first_success_profile)
    ):
        profile_path = []
        for profile_id in profile_ids:
            if (slug, profile_id) not in started_pairs:
                continue
            candidate = latest_candidate_by_pair.get((slug, profile_id))
            profile_path.append(
                {
                    "profileId": profile_id,
                    "candidateReady": candidate is not None,
                    "candidateCodeSha256": (
                        candidate.get("code_sha256") if candidate is not None else None
                    ),
                    "deferred": (slug, profile_id) in deferred_pairs,
                    "remoteAccepted": first_success_profile.get(slug) == profile_id,
                }
            )
        ladder_paths[slug] = profile_path

    def terminal_by_difficulty(level: str) -> dict[str, Any]:
        eligible_slugs = {
            str(item["titleSlug"])
            for item in accessible_problems
            if str(item.get("difficulty", "UNKNOWN")) == level
        }
        level_deferred = {slug for slug, _ in deferred_pairs} & eligible_slugs
        level_accepted = accepted & eligible_slugs
        level_awaiting = awaiting_remote_accepted & eligible_slugs
        level_submitted = submitted_slugs & eligible_slugs
        level_failed = failed_submission_slugs & eligible_slugs
        eligible_count = len(eligible_slugs)
        return {
            "eligible": eligible_count,
            "started": len(started & eligible_slugs),
            "submitted": len(level_submitted),
            "remoteAccepted": len(level_accepted),
            "failedSubmissionProblems": len(level_failed),
            "deferred": len(level_deferred),
            "awaitingRemoteAccepted": len(level_awaiting),
            "remoteAcceptanceCoverage": (
                len(level_accepted) / eligible_count if eligible_count else 0.0
            ),
        }
    return {
        "schemaVersion": 3,
        "generatedAt": utc_now(),
        "catalogSyncedAt": catalog.get("syncedAt"),
        "defaultProfile": configured_profiles.default_profile,
        "executionLadder": list(configured_profiles.execution_ladder),
        "catalogTotal": total,
        "accessibleWithoutPremium": accessible,
        "paidOnly": total - accessible,
        "archivedDetails": archived,
        "archivedReadableDetails": readable_archives,
        "archivedLockedOrUnavailable": archived - readable_archives,
        "started": len(started),
        "accepted": accepted_count,
        "deferredProblems": len({slug for slug, _ in deferred_pairs}),
        "deferredProfileAssignments": len(deferred_pairs),
        "reviewRequired": len(review_required_pairs),
        "remainingAccessible": max(accessible - accessible_accepted, 0),
        "remoteTests": len(charged_test_starts),
        "submissions": len(charged_submission_starts),
        "firstSubmissionAccepted": first_submission_accepts,
        "firstRoundAccepted": first_round_accepts,
        "firstSubmissionAcceptanceRate": first_submission_accepts / accepted_count if accepted_count else 0.0,
        "overallSubmissionAcceptanceRate": (
            accepted_count / len(charged_submission_starts)
            if charged_submission_starts
            else 0.0
        ),
        "byDifficulty": {
            level: {
                "eligible": difficulty_total[level],
                "accepted": difficulty_accepted[level],
                "remoteAcceptanceCoverage": (
                    difficulty_accepted[level] / difficulty_total[level]
                    if difficulty_total[level]
                    else 0.0
                ),
            }
            for level in sorted(difficulty_total)
        },
        "catalogByDifficulty": {
            level: {
                "all": all_difficulty_total[level],
                "free": difficulty_total[level],
                "paid": paid_difficulty_total[level],
            }
            for level in sorted(all_difficulty_total)
        },
        "experimentByDifficulty": {
            level: terminal_by_difficulty(level) for level in sorted(difficulty_total)
        },
        "failedSubmissions": {
            "attempts": len(failed_result_events),
            "uniqueProblems": len(failed_submission_slugs),
        },
        "infrastructureErrors": {
            "remoteTests": sum(
                1
                for event in infrastructure_result_events
                if event.get("type") == "remote_test_result"
            ),
            "submissions": sum(
                1
                for event in infrastructure_result_events
                if event.get("type") == "submission_result"
            ),
            "total": len(infrastructure_result_events),
            "countsAgainstModelMetrics": False,
        },
        "awaitingRemoteAccepted": len(awaiting_remote_accepted),
        "acceptedCodeDrift": sorted(accepted_code_drift, key=lambda item: item["slug"]),
        "acceptedCodeExactMatchCount": accepted_code_exact_match_count,
        "candidateCodeDrift": sorted(
            current_candidate_drift, key=lambda item: (item["slug"], item["profileId"])
        ),
        "candidateReady": len({slug for slug, _ in latest_candidate_by_pair}),
        "candidateReadyProfileAssignments": len(latest_candidate_by_pair),
        "ladderPaths": ladder_paths,
        "escalationQueueByProfile": escalation_queue,
        "unresolvedAtHighestProfile": unresolved_at_highest,
        "firstSuccessByDifficulty": {
            level: dict(sorted(counts.items()))
            for level, counts in sorted(first_success_by_difficulty.items())
        },
        "firstSuccessByProblem": dict(sorted(first_success_by_problem.items())),
        "acceptedByProfile": dict(sorted(accepted_by_profile.items())),
        "acceptedByAgent": dict(sorted(accepted_by_agent.items())),
        "profiles": profile_stats,
        "deferredByProfile": {
            profile_id: sorted(slug for slug, pid in deferred_pairs if pid == profile_id)
            for profile_id in profile_ids
        },
        "reviewRequiredByProfile": {
            profile_id: sorted(slug for slug, pid in review_required_pairs if pid == profile_id)
            for profile_id in profile_ids
        },
        "usageCoverage": {
            "startedProfileAssignments": len(started_pairs),
            "reportedProfileAssignments": len(reported_pairs & started_pairs),
            "coverage": (
                len(reported_pairs & started_pairs) / len(started_pairs) if started_pairs else 0.0
            ),
            "policy": "仅统计客户端提供且注明来源的数据；缺失值不估算",
        },
        "reviewRequiredSlugs": sorted({slug for slug, _ in review_required_pairs}),
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
        f"| 已记录本地候选 | {summary['candidateReady']} |",
        f"| Accepted | {summary['accepted']} |",
        f"| 免费题仍待远程 Accepted | {summary['awaitingRemoteAccepted']} |",
        f"| 已 defer 的题 | {summary['deferredProblems']} |",
        f"| 等待复盘的 Profile/题组合 | {summary['reviewRequired']} |",
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
        "## Profile 阶梯",
        "",
        "| Profile | 模型 | 推理档位 | 已开始 | 本地候选 | 首次成功 | defer | 提交 | Token 覆盖 |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for profile_id, values in summary["profiles"].items():
        lines.append(
            f"| {profile_id} | {values['model']} | {values['reasoningEffort']} | "
            f"{values['started']} | {values['candidateReady']} | {values['accepted']} | {values['deferred']} | "
            f"{values['submissions']} | {values['usage']['coverageOfStarted']:.2%} |"
        )
    lines.extend(
        [
            "",
            "> “首次成功 Profile”表示按既定升档流程首次获得 Accepted 的档位；高档可能继承低档失败产物，",
            "> 因此它衡量的是阶梯实验结果，不等同于各模型从空白起步的独立盲测能力。",
            "",
            "## 免费实验集难度分布",
            "",
            "| 难度 | 免费题 | 远程 Accepted | 覆盖率 |",
            "|---|---:|---:|---:|",
        ]
    )
    for level, values in summary["byDifficulty"].items():
        lines.append(
            f"| {level} | {values['eligible']} | {values['accepted']} | "
            f"{values['remoteAcceptanceCoverage']:.2%} |"
        )
    lines.extend(["", "## 首次成功 Profile × 难度", ""])
    for level, values in summary["firstSuccessByDifficulty"].items():
        distribution = "，".join(f"{profile}: {count}" for profile, count in values.items()) or "尚无"
        lines.append(f"- {level}：{distribution}")
    lines.extend(
        [
            "",
            "## 免费题流程进度 × 难度",
            "",
            "| 难度 | 已开始 | 已提交 | 远程 Accepted | 有失败提交 | 曾 defer | 待 Accepted |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for level, values in summary["experimentByDifficulty"].items():
        lines.append(
            f"| {level} | {values['started']} | {values['submitted']} | "
            f"{values['remoteAccepted']} | {values['failedSubmissionProblems']} | "
            f"{values['deferred']} | {values['awaitingRemoteAccepted']} |"
        )
    lines.extend(
        [
            "",
            f"失败正式提交：{summary['failedSubmissions']['attempts']} 次，"
            f"涉及 {summary['failedSubmissions']['uniqueProblems']} 题。",
            f"基础设施错误：远程试跑 {summary['infrastructureErrors']['remoteTests']} 次，"
            f"正式提交 {summary['infrastructureErrors']['submissions']} 次；"
            "均不计入模型提交数、失败数或通过率。",
            f"当前本地代码与 Accepted 代码哈希不同：{len(summary['acceptedCodeDrift'])} 题；"
            f"其中 {sum(1 for item in summary['acceptedCodeDrift'] if item.get('currentCandidateRecorded'))} 题"
            "已另有可追溯 candidate-ready，首次 Accepted 归因保持不变。",
            f"当前本地代码与 Accepted 代码哈希完全一致：{summary['acceptedCodeExactMatchCount']} 题。",
            f"当前本地代码与 candidate-ready 哈希漂移：{len(summary['candidateCodeDrift'])} 个 Profile/题组合。",
        ]
    )
    lines.extend(["", "## 待升级重新解题", ""])
    any_escalation = False
    for profile_id, items in summary["escalationQueueByProfile"].items():
        pending_items = [item for item in items if item["needsNewCandidate"]]
        if not pending_items:
            continue
        any_escalation = True
        lines.append(f"- {profile_id}：{len(pending_items)} 题待产出新的本地候选")
    if not any_escalation:
        lines.append("当前没有等待更高 Profile 重新解题的题目。")
    lines.extend(["", "## 最高档仍未解决", ""])
    if summary["unresolvedAtHighestProfile"]:
        grouped: dict[str, list[str]] = {}
        for item in summary["unresolvedAtHighestProfile"]:
            grouped.setdefault(item["profileId"], []).append(item["slug"])
        for profile_id, slugs in grouped.items():
            lines.append(f"- {profile_id}：{len(slugs)} 题")
    else:
        lines.append("当前没有到达最高档后仍未解决的题目。")
    lines.extend(["", "## Agent 贡献", ""])
    if summary["acceptedByAgent"]:
        for name, count in summary["acceptedByAgent"].items():
            lines.append(f"- {name}: {count}")
    else:
        lines.append("尚无 Accepted 记录。")
    lines.extend(
        [
            "",
            "## Token 数据完整性",
            "",
            f"- 覆盖率：{summary['usageCoverage']['coverage']:.2%}",
            f"- 规则：{summary['usageCoverage']['policy']}",
        ]
    )
    if summary["reviewRequiredSlugs"]:
        lines.extend(["", "## 等待复盘", ""])
        lines.extend(f"- {slug}" for slug in summary["reviewRequiredSlugs"])
    lines.append("")
    return "\n".join(lines)


def write_stats(budget: AttemptBudget, *, root: Path = ROOT) -> dict[str, Any]:
    summary = build_summary(budget, root=root)
    atomic_write_json(root / "stats" / "summary.json", summary)
    atomic_write_text(root / "stats" / "summary.md", render_markdown(summary))
    return summary
