# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:27:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        from math import comb

        result = 0
        for rows in range(n + 1):
            for columns in range(n + 1):
                if rows * n + columns * n - rows * columns == k:
                    result += comb(n, rows) * comb(n, columns)
        return result
