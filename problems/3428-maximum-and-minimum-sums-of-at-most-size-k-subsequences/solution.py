# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        mod = 1_000_000_007
        nums.sort()
        n = len(nums)
        comb = [1] * n
        for r in range(1, n):
            comb[r] = comb[r - 1] * (n - r) % mod * pow(r, mod - 2, mod) % mod
        prefix = [0] * n
        running = 0
        for r in range(n):
            running = (running + comb[r]) % mod
            prefix[r] = running
        answer = 0
        for i, value in enumerate(nums):
            ways = prefix[min(k - 1, i)]
            ways += prefix[min(k - 1, n - 1 - i)]
            answer = (answer + value * ways) % mod
        return answer
