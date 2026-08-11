# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:24:05Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def cost(valley_parity: int) -> int:
            moves = 0
            for index, value in enumerate(nums):
                if index % 2 == valley_parity:
                    neighbor = min(
                        nums[index - 1] if index else float("inf"),
                        nums[index + 1] if index + 1 < len(nums) else float("inf"),
                    )
                    moves += max(0, value - neighbor + 1)
            return moves

        return min(cost(0), cost(1))
