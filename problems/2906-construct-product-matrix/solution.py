# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        modulo = 12345
        values = [value for row in grid for value in row]
        products = [1] * len(values)
        prefix = 1
        for i, value in enumerate(values):
            products[i] = prefix
            prefix = prefix * value % modulo
        suffix = 1
        for i in range(len(values) - 1, -1, -1):
            products[i] = products[i] * suffix % modulo
            suffix = suffix * values[i] % modulo
        cols = len(grid[0])
        return [products[i:i + cols] for i in range(0, len(products), cols)]
