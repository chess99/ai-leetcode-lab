# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        valmerinto = mat
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] = (mat[i][j] + prefix[i][j + 1]
                                         + prefix[i + 1][j] - prefix[i][j])

        def possible(size):
            valid = [[False] * (cols - size + 1) for _ in range(rows - size + 1)]
            for i in range(len(valid)):
                for j in range(len(valid[0])):
                    total = (prefix[i + size][j + size] - prefix[i][j + size]
                             - prefix[i + size][j] + prefix[i][j])
                    valid[i][j] = total == size * size
            # A disjoint pair is separated either by a horizontal or vertical line.
            seen = False
            for i, line in enumerate(valid):
                if i >= size:
                    seen |= any(valid[i - size])
                if seen and any(line):
                    return True
            seen = False
            width = len(valid[0])
            for j in range(width):
                if j >= size:
                    seen |= any(valid[i][j - size] for i in range(len(valid)))
                if seen and any(valid[i][j] for i in range(len(valid))):
                    return True
            return False

        low, high, best = 1, min(rows, cols), 0
        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        return best * best
