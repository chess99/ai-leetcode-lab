# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for _, loser in edges:
            indegree[loser] += 1
        candidates = [team for team, degree in enumerate(indegree) if degree == 0]
        return candidates[0] if len(candidates) == 1 else -1
