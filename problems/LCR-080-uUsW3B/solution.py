# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                answer.append(path[:])
                return
            needed = k - len(path)
            last = n - needed + 1
            for number in range(start, last + 1):
                path.append(number)
                backtrack(number + 1)
                path.pop()

        backtrack(1)
        return answer
