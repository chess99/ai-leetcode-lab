# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:41Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        velqoradin = nums
        maximum = 0
        values = []
        for value in nums:
            maximum = max(maximum, value)
            values.append(gcd(value, maximum))
        values.sort()
        return sum(gcd(values[i], values[-1 - i]) for i in range(len(values) // 2))
