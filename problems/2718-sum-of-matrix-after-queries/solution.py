# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows, cols = set(), set()
        total = 0
        for query_type, index, value in reversed(queries):
            if query_type == 0 and index not in rows:
                total += value * (n - len(cols))
                rows.add(index)
            elif query_type == 1 and index not in cols:
                total += value * (n - len(rows))
                cols.add(index)
        return total
