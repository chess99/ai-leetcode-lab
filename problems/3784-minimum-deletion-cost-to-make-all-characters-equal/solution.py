# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import defaultdict


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        serivaldan = (s, cost)
        kept = defaultdict(int)
        total = 0
        for ch, value in zip(*serivaldan):
            kept[ch] += value
            total += value
        return total - max(kept.values())
