# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:08:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False

        side_length = total // 4
        matchsticks.sort(reverse=True)
        if not matchsticks or matchsticks[0] > side_length:
            return False

        sides = [0] * 4

        def place(index: int) -> bool:
            if index == len(matchsticks):
                return True

            stick = matchsticks[index]
            tried_lengths = set()
            for side in range(4):
                if sides[side] in tried_lengths or sides[side] + stick > side_length:
                    continue
                tried_lengths.add(sides[side])
                sides[side] += stick
                if place(index + 1):
                    return True
                sides[side] -= stick
            return False

        return place(0)
