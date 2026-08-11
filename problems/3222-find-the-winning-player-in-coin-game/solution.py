# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:47:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        moves = min(x, y // 4)
        return "Alice" if moves % 2 else "Bob"
