# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:14:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        reachable = [False] * (target + 1)
        reachable[0] = True
        for stone in stones:
            for weight in range(target, stone - 1, -1):
                reachable[weight] |= reachable[weight - stone]
        for weight in range(target, -1, -1):
            if reachable[weight]:
                return total - 2 * weight
        return 0
