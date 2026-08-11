# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:16:41Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_counts = defaultdict(int)
        for row in wall:
            position = 0
            for width in row[:-1]:
                position += width
                edge_counts[position] += 1
        return len(wall) - max(edge_counts.values(), default=0)
