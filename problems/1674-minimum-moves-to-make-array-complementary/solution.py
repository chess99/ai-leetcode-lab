# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        changes = [0] * (2 * limit + 2)

        for index in range(len(nums) // 2):
            first = nums[index]
            second = nums[-1 - index]
            low, high = sorted((first, second))
            pair_sum = first + second

            changes[2] += 2
            changes[low + 1] -= 1
            changes[pair_sum] -= 1
            changes[pair_sum + 1] += 1
            changes[high + limit + 1] += 1

        minimum_moves = float("inf")
        moves = 0
        for target_sum in range(2, 2 * limit + 1):
            moves += changes[target_sum]
            minimum_moves = min(minimum_moves, moves)

        return minimum_moves
