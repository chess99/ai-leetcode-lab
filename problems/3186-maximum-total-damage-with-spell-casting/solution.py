# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from collections import Counter
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = Counter(power)
        values = sorted(counts)
        dp = [0] * (len(values) + 1)
        for index, value in enumerate(values, 1):
            previous = bisect_right(values, value - 3, 0, index - 1)
            dp[index] = max(dp[index - 1], dp[previous] + value * counts[value])
        return dp[-1]
