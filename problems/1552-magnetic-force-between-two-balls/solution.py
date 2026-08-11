# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:56:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def feasible(distance):
            count = 1; last = position[0]
            for value in position[1:]:
                if value - last >= distance: count += 1; last = value
            return count >= m
        low, high = 1, position[-1] - position[0]
        while low <= high:
            middle = (low + high) // 2
            if feasible(middle): low = middle + 1
            else: high = middle - 1
        return high
