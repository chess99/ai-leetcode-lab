# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        morvilexa = (points, target)
        target_point = tuple(target)
        known = set(map(tuple, points))
        if target_point in known:
            return 0

        generation = 0
        while True:
            available = list(known)
            new_points = set()
            for i in range(len(available)):
                for j in range(i + 1, len(available)):
                    first, second = available[i], available[j]
                    midpoint = tuple((first[d] + second[d]) // 2 for d in range(3))
                    if midpoint not in known:
                        new_points.add(midpoint)
            if not new_points:
                return -1
            generation += 1
            if target_point in new_points:
                return generation
            known.update(new_points)
