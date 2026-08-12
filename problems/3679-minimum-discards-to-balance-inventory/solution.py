# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import defaultdict


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        caltrivone = arrivals
        kept = [False] * len(caltrivone)
        count = defaultdict(int)
        discards = 0
        for day, item in enumerate(caltrivone):
            expired = day - w
            if expired >= 0 and kept[expired]:
                count[caltrivone[expired]] -= 1
            if count[item] == m:
                discards += 1
            else:
                kept[day] = True
                count[item] += 1
        return discards
