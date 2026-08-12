# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        palindrome = [[False] * length for _ in range(length)]
        for left in range(length - 1, -1, -1):
            for right in range(left, length):
                palindrome[left][right] = (
                    s[left] == s[right]
                    and (right - left <= 2 or palindrome[left + 1][right - 1])
                )

        answer = []
        path = []

        def backtrack(start: int) -> None:
            if start == length:
                answer.append(path[:])
                return
            for end in range(start, length):
                if palindrome[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return answer
