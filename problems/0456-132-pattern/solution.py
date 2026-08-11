# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:06:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        middle = float("-inf")
        candidates = []

        for value in reversed(nums):
            if value < middle:
                return True
            while candidates and value > candidates[-1]:
                middle = candidates.pop()
            candidates.append(value)

        return False
