# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder_to_latest_index = {0: -1}
        required_remainder = sum(nums) % p
        if required_remainder == 0:
            return 0

        shortest = len(nums)
        prefix_remainder = 0
        for index, value in enumerate(nums):
            prefix_remainder = (prefix_remainder + value) % p
            needed_prefix = (prefix_remainder - required_remainder) % p
            if needed_prefix in remainder_to_latest_index:
                shortest = min(shortest, index - remainder_to_latest_index[needed_prefix])
            remainder_to_latest_index[prefix_remainder] = index

        return shortest if shortest < len(nums) else -1
