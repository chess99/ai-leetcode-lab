# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        moves = {'A': 0, 'B': 0}
        run_start = 0

        for i in range(1, len(colors) + 1):
            if i == len(colors) or colors[i] != colors[run_start]:
                moves[colors[run_start]] += max(0, i - run_start - 2)
                run_start = i

        return moves['A'] > moves['B']
