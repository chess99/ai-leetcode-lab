# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:12:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        count = len(stones)
        maximum_moves = max(
            stones[-1] - stones[1] - (count - 2),
            stones[-2] - stones[0] - (count - 2),
        )

        minimum_moves = count
        left = 0
        for right, stone in enumerate(stones):
            while stone - stones[left] >= count:
                left += 1
            in_window = right - left + 1
            if in_window == count - 1 and stone - stones[left] == count - 2:
                minimum_moves = min(minimum_moves, 2)
            else:
                minimum_moves = min(minimum_moves, count - in_window)
        return [minimum_moves, maximum_moves]
