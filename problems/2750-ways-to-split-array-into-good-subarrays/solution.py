# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        answer = 1
        previous_one = None
        for index, value in enumerate(nums):
            if value:
                if previous_one is not None:
                    answer = answer * (index - previous_one) % 1_000_000_007
                previous_one = index
        return answer if previous_one is not None else 0
