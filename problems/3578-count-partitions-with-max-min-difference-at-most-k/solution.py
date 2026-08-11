# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 1_000_000_007
        n = len(nums)
        dp = [0] * (n + 1); prefix = [0] * (n + 1); dp[0] = prefix[0] = 1
        lo = 0; mn = deque(); mx = deque()
        for r, value in enumerate(nums):
            while mn and nums[mn[-1]] >= value: mn.pop()
            while mx and nums[mx[-1]] <= value: mx.pop()
            mn.append(r); mx.append(r)
            while nums[mx[0]] - nums[mn[0]] > k:
                if mn[0] == lo: mn.popleft()
                if mx[0] == lo: mx.popleft()
                lo += 1
            dp[r + 1] = (prefix[r] - (prefix[lo - 1] if lo else 0)) % mod
            prefix[r + 1] = (prefix[r] + dp[r + 1]) % mod
        return dp[n]
