# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        cavolinexy = (nums, cost, k)
        n = len(nums)
        prefix_nums = [0]
        prefix_cost = [0]
        for value, weight in zip(nums, cost):
            prefix_nums.append(prefix_nums[-1] + value)
            prefix_cost.append(prefix_cost[-1] + weight)

        # The k * group_index terms equal k * total_cost plus, for every
        # internal cut p, k times the cost suffix after p.
        dp = [10 ** 30] * (n + 1)
        dp[0] = k * prefix_cost[n]
        for right in range(1, n + 1):
            nums_sum = prefix_nums[right]
            for left in range(right):
                cut_cost = (0 if left == 0
                            else k * (prefix_cost[n] - prefix_cost[left]))
                candidate = (dp[left] + cut_cost
                             + nums_sum * (prefix_cost[right]
                                           - prefix_cost[left]))
                if candidate < dp[right]:
                    dp[right] = candidate
        return dp[n]
