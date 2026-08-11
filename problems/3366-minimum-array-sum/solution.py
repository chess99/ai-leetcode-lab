# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        inf = float('inf')
        dp = [[inf] * (op2 + 1) for _ in range(op1 + 1)]
        dp[0][0] = 0
        for value in nums:
            nxt = [[inf] * (op2 + 1) for _ in range(op1 + 1)]
            half = (value + 1) // 2
            for used1 in range(op1 + 1):
                for used2 in range(op2 + 1):
                    base = dp[used1][used2]
                    if base == inf:
                        continue
                    nxt[used1][used2] = min(nxt[used1][used2], base + value)
                    if used1 < op1:
                        nxt[used1 + 1][used2] = min(nxt[used1 + 1][used2], base + half)
                    if used2 < op2 and value >= k:
                        nxt[used1][used2 + 1] = min(nxt[used1][used2 + 1], base + value - k)
                    if used1 < op1 and used2 < op2:
                        best = inf
                        if value >= k:
                            best = min(best, (value - k + 1) // 2)
                        if half >= k:
                            best = min(best, half - k)
                        if best < inf:
                            nxt[used1 + 1][used2 + 1] = min(nxt[used1 + 1][used2 + 1], base + best)
            dp = nxt
        return min(map(min, dp))
