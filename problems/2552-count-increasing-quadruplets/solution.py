# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        size = len(nums)
        left_smaller = [0] * size
        answer = 0
        for second in range(size):
            right_larger = 0
            for third in range(size - 1, second, -1):
                if nums[third] > nums[second]:
                    right_larger += 1
                elif nums[third] < nums[second]:
                    answer += left_smaller[third] * right_larger
            for third in range(second + 1, size):
                if nums[second] < nums[third]:
                    left_smaller[third] += 1
        return answer
