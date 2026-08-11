# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def knightDialer(self, n: int) -> int:
        modulo = 1_000_000_007
        moves = ((4, 6), (6, 8), (7, 9), (4, 8), (0, 3, 9), (),
                 (0, 1, 7), (2, 6), (1, 3), (2, 4))
        counts = [1] * 10
        for _ in range(n - 1):
            counts = [sum(counts[previous] for previous in moves[digit]) % modulo
                      for digit in range(10)]
        return sum(counts) % modulo
