# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) == 1:
            return True
        if stones[1] != 1:
            return False
        jumps = {stone: set() for stone in stones}
        jumps[0].add(0)
        target = stones[-1]
        for stone in stones:
            for previous in jumps[stone]:
                for step in (previous - 1, previous, previous + 1):
                    if step <= 0:
                        continue
                    destination = stone + step
                    if destination == target:
                        return True
                    if destination in jumps:
                        jumps[destination].add(step)
        return False
