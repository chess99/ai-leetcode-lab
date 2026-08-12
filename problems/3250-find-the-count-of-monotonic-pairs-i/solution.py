# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 1_000_000_007
        dp = [1] * (nums[0] + 1)
        for previous_num, current_num in zip(nums, nums[1:]):
            prefix = []
            running = 0
            for ways in dp:
                running = (running + ways) % mod
                prefix.append(running)

            new = [0] * (current_num + 1)
            shift = previous_num - current_num
            for current in range(current_num + 1):
                limit = min(current, current + shift)
                if limit >= 0:
                    new[current] = prefix[min(limit, len(prefix) - 1)]
            dp = new
        return sum(dp) % mod
