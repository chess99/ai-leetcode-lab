# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        from collections import defaultdict
        rows, cols = len(matrix), len(matrix[0])
        answer = 0
        for top in range(rows):
            sums = [0] * cols
            for bottom in range(top, rows):
                for col in range(cols):
                    sums[col] += matrix[bottom][col]
                counts = defaultdict(int, {0: 1})
                prefix = 0
                for value in sums:
                    prefix += value
                    answer += counts[prefix - target]
                    counts[prefix] += 1
        return answer
