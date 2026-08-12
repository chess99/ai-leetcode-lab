# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        neighbors = [[] for _ in scores]
        for first, second in edges:
            neighbors[first].append(second)
            neighbors[second].append(first)
        for node in range(len(scores)):
            neighbors[node] = sorted(
                neighbors[node], key=lambda neighbor: scores[neighbor], reverse=True
            )[:3]

        answer = -1
        for second, third in edges:
            for first in neighbors[second]:
                for fourth in neighbors[third]:
                    if len({first, second, third, fourth}) == 4:
                        answer = max(
                            answer,
                            scores[first] + scores[second]
                            + scores[third] + scores[fourth],
                        )
        return answer
