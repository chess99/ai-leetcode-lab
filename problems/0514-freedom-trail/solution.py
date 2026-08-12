# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:18Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        positions = defaultdict(list)
        for index, char in enumerate(ring):
            positions[char].append(index)
        current = {0: 0}
        size = len(ring)
        for char in key:
            following = {}
            for target in positions[char]:
                following[target] = min(cost + min(abs(source-target), size-abs(source-target)) + 1
                                        for source, cost in current.items())
            current = following
        return min(current.values())
