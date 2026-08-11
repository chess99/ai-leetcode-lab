# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:31:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = {(row, column): 1.0}
        moves = ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2))
        for _ in range(k):
            next_dp = {}
            for (r, c), probability in dp.items():
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n: next_dp[nr, nc] = next_dp.get((nr, nc), 0) + probability / 8
            dp = next_dp
        return sum(dp.values())
