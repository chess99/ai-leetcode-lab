# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        best = None
        cx, cy = center
        for x, y, quality in towers:
            if abs(x - cx) + abs(y - cy) <= radius:
                candidate = (-quality, x, y)
                if best is None or candidate < best:
                    best = candidate
        return [-1, -1] if best is None else [best[1], best[2]]
