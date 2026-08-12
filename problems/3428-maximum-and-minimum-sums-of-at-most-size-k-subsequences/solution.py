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
        ways = [0] * n
        combinations = [0] * k
        combinations[0] = 1
        ways[0] = 1
        for size in range(1, n):
            upper = min(k - 1, size)
            for chosen in range(upper, 0, -1):
                combinations[chosen] = (
                    combinations[chosen] + combinations[chosen - 1]
                ) % mod
            ways[size] = sum(combinations[: upper + 1]) % mod
        answer = 0
        for i, value in enumerate(nums):
            count = ways[i] + ways[n - 1 - i]
            answer = (answer + value * count) % mod
        return answer
