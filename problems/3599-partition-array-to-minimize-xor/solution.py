# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        quendravil = (nums, k)
        prefix = [0]
        for value in nums: prefix.append(prefix[-1] ^ value)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for groups in range(1, k + 1):
            nxt = [float('inf')] * (n + 1)
            for end in range(groups, n + 1):
                for start in range(groups - 1, end):
                    nxt[end] = min(nxt[end], max(dp[start], prefix[end] ^ prefix[start]))
            dp = nxt
        return dp[n]
