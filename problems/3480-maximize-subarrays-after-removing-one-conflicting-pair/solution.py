# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:39:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        by_right = [[] for _ in range(n + 1)]
        for pair_id, (first, second) in enumerate(conflictingPairs):
            left, right = sorted((first, second))
            by_right[right].append((left, pair_id))

        largest = (0, -1)
        second = (0, -1)
        gains = [0] * len(conflictingPairs)
        base = 0
        for right in range(1, n + 1):
            for item in by_right[right]:
                if item[0] > largest[0]:
                    second = largest
                    largest = item
                elif item[0] > second[0]:
                    second = item
            base += right - largest[0]
            if largest[1] >= 0:
                gains[largest[1]] += largest[0] - second[0]
        return base + max(gains, default=0)
