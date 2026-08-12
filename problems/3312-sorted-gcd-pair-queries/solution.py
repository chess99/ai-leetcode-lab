# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:34Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maximum = max(nums)
        frequencies = [0] * (maximum + 1)
        for value in nums:
            frequencies[value] += 1
        exact = [0] * (maximum + 1)
        for divisor in range(maximum, 0, -1):
            count = sum(frequencies[multiple]
                        for multiple in range(divisor, maximum + 1, divisor))
            pairs = count * (count - 1) // 2
            for multiple in range(divisor * 2, maximum + 1, divisor):
                pairs -= exact[multiple]
            exact[divisor] = pairs
        cumulative = []
        total = 0
        for divisor in range(1, maximum + 1):
            total += exact[divisor]
            cumulative.append(total)
        return [bisect_right(cumulative, query) + 1 for query in queries]
