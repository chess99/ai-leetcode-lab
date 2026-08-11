# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:27Z
# Experiment: ai-leetcode-lab, round 1


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1 and maxDoubles:
            if target % 2:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
            moves += 1

        return moves + target - 1
