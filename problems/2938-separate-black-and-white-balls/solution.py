# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = moves = 0
        for ch in s:
            if ch == "1":
                ones += 1
            else:
                moves += ones
        return moves
