# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:46:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [float(poured)]
        for _ in range(query_row):
            nxt = [0.0] * (len(row)+1)
            for i, amount in enumerate(row):
                if amount > 1: nxt[i] += (amount-1)/2; nxt[i+1] += (amount-1)/2
            row = nxt
        return min(1.0, row[query_glass])
