# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        groups = gcd(len(arr), k)
        operations = 0
        for start in range(groups):
            values = sorted(arr[start::groups])
            median = values[len(values) // 2]
            operations += sum(abs(value - median) for value in values)
        return operations
