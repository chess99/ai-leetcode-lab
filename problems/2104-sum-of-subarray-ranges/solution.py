# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def total_extremes(is_maximum: bool) -> int:
            stack = []
            total = 0
            sentinel = float('inf') if is_maximum else float('-inf')

            for i in range(len(nums) + 1):
                current = nums[i] if i < len(nums) else sentinel
                while stack and (
                    nums[stack[-1]] <= current if is_maximum else nums[stack[-1]] >= current
                ):
                    middle = stack.pop()
                    left = stack[-1] if stack else -1
                    total += nums[middle] * (middle - left) * (i - middle)
                stack.append(i)
            return total

        return total_extremes(True) - total_extremes(False)
