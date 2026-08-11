# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List

class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        min_x = min(x for x, _ in coords); max_x = max(x for x, _ in coords)
        min_y = min(y for _, y in coords); max_y = max(y for _, y in coords)
        by_x, by_y = defaultdict(list), defaultdict(list)
        for x, y in coords: by_x[x].append(y); by_y[y].append(x)
        ans = 0
        for x, ys in by_x.items():
            if len(ys) > 1: ans = max(ans, (max(ys)-min(ys))*max(x-min_x, max_x-x))
        for y, xs in by_y.items():
            if len(xs) > 1: ans = max(ans, (max(xs)-min(xs))*max(y-min_y, max_y-y))
        return ans or -1
