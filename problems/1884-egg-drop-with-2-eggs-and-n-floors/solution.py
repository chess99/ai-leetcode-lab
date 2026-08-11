# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def twoEggDrop(self, n: int) -> int:
        moves = 0
        covered_floors = 0
        while covered_floors < n:
            moves += 1
            covered_floors += moves
        return moves
