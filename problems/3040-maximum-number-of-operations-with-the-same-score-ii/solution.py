# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from functools import cache
import sys
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        sys.setrecursionlimit(10_000)
        def solve(target: int) -> int:
            @cache
            def dp(left: int, right: int) -> int:
                if right - left < 1:
                    return 0
                best = 0
                if nums[left] + nums[left + 1] == target:
                    best = max(best, 1 + dp(left + 2, right))
                if nums[right - 1] + nums[right] == target:
                    best = max(best, 1 + dp(left, right - 2))
                if nums[left] + nums[right] == target:
                    best = max(best, 1 + dp(left + 1, right - 1))
                return best

            return dp(0, len(nums) - 1)

        return max(solve(nums[0] + nums[1]), solve(nums[-2] + nums[-1]), solve(nums[0] + nums[-1]))
