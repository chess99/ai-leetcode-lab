# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left_zeros = 0
        right_ones = sum(nums)
        best_score = -1
        answer = []

        for division in range(len(nums) + 1):
            score = left_zeros + right_ones
            if score > best_score:
                best_score = score
                answer = [division]
            elif score == best_score:
                answer.append(division)

            if division < len(nums):
                if nums[division] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1

        return answer
