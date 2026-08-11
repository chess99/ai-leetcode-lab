# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:11:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index - 1]:
                    continue
                candidate = candidates[index]
                if candidate > remaining:
                    break
                path.append(candidate)
                backtrack(index + 1, remaining - candidate)
                path.pop()

        backtrack(0, target)
        return result
