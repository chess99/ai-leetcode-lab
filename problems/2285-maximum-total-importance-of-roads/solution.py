# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:23Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for city_a, city_b in roads:
            degrees[city_a] += 1
            degrees[city_b] += 1

        return sum(degree * value for degree, value in zip(sorted(degrees), range(1, n + 1)))
