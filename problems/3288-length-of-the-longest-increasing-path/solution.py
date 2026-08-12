# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:32Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        pivot_x, pivot_y = coordinates[k]

        def longest(points):
            tails = []
            for _, y in sorted(points, key=lambda point: (point[0], -point[1])):
                position = bisect_left(tails, y)
                if position == len(tails):
                    tails.append(y)
                else:
                    tails[position] = y
            return len(tails)

        lower = [point for point in coordinates
                 if point[0] < pivot_x and point[1] < pivot_y]
        upper = [[-point[0], -point[1]] for point in coordinates
                 if point[0] > pivot_x and point[1] > pivot_y]
        return longest(lower) + 1 + longest(upper)
