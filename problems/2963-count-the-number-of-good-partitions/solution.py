# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        modulus = 10 ** 9 + 7
        last = {value: index for index, value in enumerate(nums)}
        end = 0
        cuts = 0
        for index, value in enumerate(nums[:-1]):
            end = max(end, last[value])
            if index == end:
                cuts += 1
        return pow(2, cuts, modulus)
