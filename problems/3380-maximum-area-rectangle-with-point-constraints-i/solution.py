# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
from itertools import combinations
from typing import List


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        point_set = {tuple(point) for point in points}
        answer = -1
        xs = sorted({x for x, _ in point_set})
        ys = sorted({y for _, y in point_set})
        for x1, x2 in combinations(xs, 2):
            for y1, y2 in combinations(ys, 2):
                corners = {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
                if not corners <= point_set:
                    continue
                if any((x, y) not in corners and x1 <= x <= x2 and y1 <= y <= y2 for x, y in point_set):
                    continue
                answer = max(answer, (x2 - x1) * (y2 - y1))
        return answer
