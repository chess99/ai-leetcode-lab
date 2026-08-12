# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []
        path = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                answer.append(path[:])
                return
            for index in range(start, len(candidates)):
                number = candidates[index]
                if number > remaining:
                    break
                path.append(number)
                backtrack(index, remaining - number)
                path.pop()

        backtrack(0, target)
        return answer
