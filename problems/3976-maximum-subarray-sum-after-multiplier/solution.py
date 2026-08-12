# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        mavireltho = (nums, k)

        def solve(transform):
            before = active = after = -float('inf')
            answer = -float('inf')
            for value in nums:
                changed = transform(value)
                next_before = max(value, before + value)
                next_active = max(changed, before + changed, active + changed)
                next_after = max(value, active + value, after + value)
                before, active, after = next_before, next_active, next_after
                answer = max(answer, active, after)
            return answer

        def divide(value):
            return value // k if value >= 0 else -((-value) // k)

        return max(solve(lambda value: value * k), solve(divide))
