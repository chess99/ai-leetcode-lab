# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:03:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = index = 0
        while index < len(s):
            if s[index] == 'X':
                moves += 1
                index += 3
            else:
                index += 1
        return moves
