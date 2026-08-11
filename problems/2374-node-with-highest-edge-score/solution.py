# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:09Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0] * len(edges)
        for source, target in enumerate(edges):
            scores[target] += source
        return max(range(len(edges)), key=lambda node: scores[node])
