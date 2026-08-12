# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        invalid = last_minimum = last_maximum = -1
        answer = 0
        for index, value in enumerate(nums):
            if value < minK or value > maxK:
                invalid = index
            if value == minK:
                last_minimum = index
            if value == maxK:
                last_maximum = index
            answer += max(0, min(last_minimum, last_maximum) - invalid)
        return answer
