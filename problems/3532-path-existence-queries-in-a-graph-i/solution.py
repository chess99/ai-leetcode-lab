# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        group = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                group += 1
            component[i] = group
        return [component[u] == component[v] for u, v in queries]
