# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:44Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        infinity = len(nums) + 1
        dp = [infinity] * 1024
        dp[0] = 0
        for offset in range(k):
            values = Counter(nums[offset::k])
            group_size = sum(values.values())
            baseline = min(dp) + group_size
            following = [baseline] * 1024
            for xor_value in range(1024):
                for value, frequency in values.items():
                    following[xor_value] = min(
                        following[xor_value],
                        dp[xor_value ^ value] + group_size - frequency)
            dp = following
        return dp[0]
