# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:13:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        first_index = {0: -1}
        remainder = 0
        for index, number in enumerate(nums):
            remainder = (remainder + number) % k
            if remainder in first_index:
                if index - first_index[remainder] >= 2:
                    return True
            else:
                first_index[remainder] = index
        return False
