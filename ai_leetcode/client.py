from __future__ import annotations

import json
import socket
import time
from dataclasses import dataclass
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .config import Credentials, ExperimentConfig


CATALOG_QUERY = """
query problemsetQuestionListV2(
  $filters: QuestionFilterInput,
  $limit: Int,
  $searchKeyword: String,
  $skip: Int,
  $sortBy: QuestionSortByInput,
  $categorySlug: String
) {
  problemsetQuestionListV2(
    filters: $filters,
    limit: $limit,
    searchKeyword: $searchKeyword,
    skip: $skip,
    sortBy: $sortBy,
    categorySlug: $categorySlug
  ) {
    questions {
      id
      titleSlug
      title
      translatedTitle
      questionFrontendId
      paidOnly
      difficulty
      topicTags { name slug nameTranslated }
      status
      frequency
      acRate
      contestPoint
    }
    totalLength
    finishedLength
    hasMore
  }
}
"""


DETAIL_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    translatedTitle
    content
    translatedContent
    isPaidOnly
    difficulty
    likes
    dislikes
    exampleTestcases
    sampleTestCase
    enableRunCode
    metaData
    codeSnippets { lang langSlug code }
    stats
    topicTags { name slug translatedName }
  }
}
"""


AUTH_QUERY = """
query globalData {
  userStatus {
    isPremium
    isVerified
    username
    avatar
    isSignedIn
  }
}
"""


class ApiError(RuntimeError):
    def __init__(self, message: str, *, infrastructure: bool = False, authentication: bool = False):
        super().__init__(message)
        self.infrastructure = infrastructure
        self.authentication = authentication


@dataclass(frozen=True)
class JudgeTask:
    task_id: str
    expected_id: str | None = None


class LeetCodeClient:
    def __init__(self, config: ExperimentConfig, credentials: Credentials | None = None):
        self.config = config
        self.credentials = credentials

    def _headers(self, referer: str, authenticated: bool) -> dict[str, str]:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Origin": self.config.endpoint,
            "Referer": referer,
            "User-Agent": "ai-leetcode-lab/0.1 (+local experiment)",
            "X-Requested-With": "XMLHttpRequest",
        }
        if authenticated:
            if not self.credentials:
                raise ApiError("缺少 LeetCode 凭证", authentication=True)
            headers["Cookie"] = self.credentials.cookie_header
            headers["X-CSRFToken"] = self.credentials.csrf_token
        return headers

    def _request_json(
        self,
        path: str,
        *,
        method: str = "GET",
        payload: dict[str, Any] | None = None,
        referer: str | None = None,
        authenticated: bool = False,
        retries: int = 2,
    ) -> dict[str, Any]:
        url = path if path.startswith("http") else f"{self.config.endpoint}{path}"
        data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
        last_error: Exception | None = None
        for attempt in range(retries + 1):
            request = Request(
                url,
                data=data,
                method=method,
                headers=self._headers(referer or self.config.endpoint, authenticated),
            )
            try:
                with urlopen(request, timeout=30) as response:
                    raw = response.read().decode("utf-8")
                    value = json.loads(raw)
                    if not isinstance(value, dict):
                        raise ApiError("接口返回了非对象 JSON", infrastructure=True)
                    return value
            except HTTPError as exc:
                body = exc.read().decode("utf-8", errors="replace")[:1000]
                if exc.code in (401, 403):
                    raise ApiError("LeetCode 登录已失效或无权访问", authentication=True) from exc
                last_error = ApiError(f"LeetCode HTTP {exc.code}: {body}", infrastructure=exc.code >= 500 or exc.code == 429)
                if exc.code not in (429, 500, 502, 503, 504) or attempt >= retries:
                    raise last_error from exc
            except (URLError, TimeoutError, socket.timeout, json.JSONDecodeError) as exc:
                last_error = ApiError(f"LeetCode 网络或响应异常：{exc}", infrastructure=True)
                if attempt >= retries:
                    raise last_error from exc
            time.sleep(1.0 + attempt * 1.5)
        raise ApiError(f"LeetCode 请求失败：{last_error}", infrastructure=True)

    def graphql(
        self,
        query: str,
        variables: dict[str, Any],
        operation_name: str,
        *,
        authenticated: bool = False,
        referer: str | None = None,
    ) -> dict[str, Any]:
        result = self._request_json(
            "/graphql/",
            method="POST",
            payload={"query": query, "variables": variables, "operationName": operation_name},
            referer=referer or f"{self.config.endpoint}/problemset/",
            authenticated=authenticated,
        )
        if result.get("errors"):
            message = "; ".join(str(item.get("message", item)) for item in result["errors"])
            raise ApiError(f"GraphQL 错误：{message}", infrastructure=False)
        data = result.get("data")
        if not isinstance(data, dict):
            raise ApiError("GraphQL 响应缺少 data", infrastructure=True)
        return data

    def check_auth(self) -> dict[str, Any]:
        data = self.graphql(AUTH_QUERY, {}, "globalData", authenticated=True)
        status = data.get("userStatus") or {}
        if not status.get("isSignedIn"):
            raise ApiError("LeetCode Cookie 未登录", authentication=True)
        return status

    def list_questions(self, skip: int, limit: int, *, authenticated: bool) -> dict[str, Any]:
        data = self.graphql(
            CATALOG_QUERY,
            {"skip": skip, "limit": limit},
            "problemsetQuestionListV2",
            authenticated=authenticated,
        )
        result = data.get("problemsetQuestionListV2")
        if not isinstance(result, dict):
            raise ApiError("题库列表响应结构已变化", infrastructure=True)
        return result

    def get_question(self, slug: str, *, authenticated: bool = False) -> dict[str, Any]:
        data = self.graphql(
            DETAIL_QUERY,
            {"titleSlug": slug},
            "questionData",
            authenticated=authenticated,
            referer=f"{self.config.endpoint}/problems/{slug}/",
        )
        question = data.get("question")
        if not isinstance(question, dict):
            raise ApiError(f"找不到题目：{slug}")
        return question

    def run_code(self, slug: str, question_id: int, language: str, code: str, test_input: str) -> JudgeTask:
        result = self._request_json(
            f"/problems/{slug}/interpret_solution/",
            method="POST",
            payload={
                "data_input": test_input,
                "lang": language,
                "question_id": question_id,
                "test_mode": False,
                "typed_code": code,
            },
            referer=f"{self.config.endpoint}/problems/{slug}/",
            authenticated=True,
        )
        if result.get("error"):
            raise ApiError(f"远程试跑被拒绝：{result['error']}", infrastructure="too soon" in str(result["error"]).lower())
        task_id = result.get("interpret_id")
        if task_id is None:
            raise ApiError(f"远程试跑响应缺少 interpret_id：{result}", infrastructure=True)
        expected_id = result.get("interpret_expected_id")
        return JudgeTask(str(task_id), str(expected_id) if expected_id is not None else None)

    def submit_code(self, slug: str, question_id: int, language: str, code: str) -> JudgeTask:
        result = self._request_json(
            f"/problems/{slug}/submit/",
            method="POST",
            payload={
                "judge_type": "large",
                "lang": language,
                "question_id": question_id,
                "test_mode": False,
                "typed_code": code,
            },
            referer=f"{self.config.endpoint}/problems/{slug}/",
            authenticated=True,
        )
        if result.get("error"):
            raise ApiError(f"正式提交被拒绝：{result['error']}", infrastructure="too soon" in str(result["error"]).lower())
        task_id = result.get("submission_id")
        if task_id is None:
            raise ApiError(f"提交响应缺少 submission_id：{result}", infrastructure=True)
        return JudgeTask(str(task_id))

    def poll_judge(self, task_id: str) -> dict[str, Any]:
        started = time.monotonic()
        while True:
            result = self._request_json(
                f"/submissions/detail/{task_id}/check/",
                referer=f"{self.config.endpoint}/submissions/detail/{task_id}/",
                authenticated=True,
                retries=1,
            )
            if result.get("state") == "SUCCESS":
                return result
            if time.monotonic() - started >= self.config.attempt_budget.poll_timeout_seconds:
                raise ApiError(f"判题轮询超时（任务 {task_id}）", infrastructure=True)
            time.sleep(self.config.attempt_budget.poll_interval_seconds)
