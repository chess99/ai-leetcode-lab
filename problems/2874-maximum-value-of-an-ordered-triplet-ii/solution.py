# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        best_left = nums[0]
        best_difference = 0
        answer = 0
        for value in nums[1:]:
            answer = max(answer, best_difference * value)
            best_difference = max(best_difference, best_left - value)
            best_left = max(best_left, value)
        return answer
