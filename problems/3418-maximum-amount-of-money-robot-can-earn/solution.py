# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins[0])
        neg_inf = -10**30
        dp = [[neg_inf] * 3 for _ in range(n)]
        for i, row in enumerate(coins):
            for j, value in enumerate(row):
                current = [neg_inf] * 3
                if i == 0 and j == 0:
                    current = [value, 0, neg_inf]
                else:
                    for source in ((dp[j] if i else [neg_inf] * 3), (dp[j - 1] if j else [neg_inf] * 3)):
                        for used, total in enumerate(source):
                            current[used] = max(current[used], total + value)
                            if used < 2:
                                current[used + 1] = max(current[used + 1], total)
                dp[j] = current
        return max(dp[-1])
