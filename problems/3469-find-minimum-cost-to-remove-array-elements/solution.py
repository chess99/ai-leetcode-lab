# AI solution attribution
# Initial creator: Codex Desktop / gpt-5.6-terra / medium / terra-medium
# Current repair: Codex Desktop / gpt-5.6-sol / medium / sol-medium
# Terra handoff: round 1 submission failed with Memory Limit Exceeded
# Created: 2026-08-11T21:59:19Z
# Experiment: ai-leetcode-lab
from typing import List


class Solution:
    def minCost(self, nums: List[int]) -> int:
        xantreloqu = nums
        n = len(xantreloqu)

        # Before index i, exactly one element remains.  dp[j] is the
        # minimum cost when that element is xantreloqu[j].
        dp = [0]
        i = 1

        while i + 1 < n:
            first = xantreloqu[i]
            second = xantreloqu[i + 1]

            keep_first = min(
                dp[j] + max(xantreloqu[j], second) for j in range(i)
            )
            keep_second = min(
                dp[j] + max(xantreloqu[j], first) for j in range(i)
            )

            remove_both = max(first, second)
            dp = [cost + remove_both for cost in dp]
            dp.extend((keep_first, keep_second))
            i += 2

        if i < n:
            return min(
                dp[j] + max(xantreloqu[j], xantreloqu[i])
                for j in range(i)
            )

        return min(dp[j] + xantreloqu[j] for j in range(i))
