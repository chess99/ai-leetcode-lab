# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        removals_left = len(nums) - k

        for value in nums:
            while stack and stack[-1] > value and removals_left:
                stack.pop()
                removals_left -= 1
            stack.append(value)

        return stack[:k]
