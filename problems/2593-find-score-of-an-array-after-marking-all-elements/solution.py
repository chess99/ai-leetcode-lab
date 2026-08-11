# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [False] * len(nums)
        score = 0
        for value, index in sorted((value, index) for index, value in enumerate(nums)):
            if marked[index]:
                continue
            score += value
            for neighbor in (index - 1, index, index + 1):
                if 0 <= neighbor < len(nums):
                    marked[neighbor] = True
        return score
