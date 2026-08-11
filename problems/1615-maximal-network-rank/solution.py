# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        links = set()
        for a, b in roads:
            degree[a] += 1; degree[b] += 1; links.add((min(a, b), max(a, b)))
        return max(degree[a] + degree[b] - ((a, b) in links) for a in range(n) for b in range(a + 1, n))
