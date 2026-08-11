# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:07:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(player):
            return sum(value * (2 if 10 in player[max(0, i-2):i] else 1) for i, value in enumerate(player))
        a, b = score(player1), score(player2)
        return 1 if a > b else (2 if b > a else 0)
