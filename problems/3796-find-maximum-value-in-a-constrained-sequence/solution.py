# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        zorimnacle = (n, restrictions, diff)
        infinity = 10**30
        bound = [infinity] * n
        bound[0] = 0
        for index, maximum in restrictions:
            bound[index] = min(bound[index], maximum)
        for i in range(1, n):
            bound[i] = min(bound[i], bound[i - 1] + diff[i - 1])
        for i in range(n - 2, -1, -1):
            bound[i] = min(bound[i], bound[i + 1] + diff[i])
        return max(bound)
