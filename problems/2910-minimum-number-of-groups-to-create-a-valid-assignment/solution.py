# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        counts = list(Counter(balls).values())
        for size in range(min(counts), 0, -1):
            if all(count // size >= (count + size) // (size + 1) for count in counts):
                return sum((count + size) // (size + 1) for count in counts)
        return len(balls)
