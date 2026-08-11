# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        min_x, max_x = {}, {}
        min_y, max_y = {}, {}
        for x, y in buildings:
            min_x[y] = min(min_x.get(y, x), x)
            max_x[y] = max(max_x.get(y, x), x)
            min_y[x] = min(min_y.get(x, y), y)
            max_y[x] = max(max_y.get(x, y), y)
        return sum(min_x[y] < x < max_x[y] and min_y[x] < y < max_y[x] for x, y in buildings)
