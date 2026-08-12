# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import Counter


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def one_dim(values: List[int]) -> bool:
            total = sum(values)
            left = 0
            seen = Counter()
            remain = Counter(values)
            for cut in range(1, len(values)):
                x = values[cut - 1]
                left += x; seen[x] += 1; remain[x] -= 1
                right = total - left
                if left == right:
                    return True
                # In a one-cell-wide rectangle, only an endpoint can vanish.
                if left > right:
                    d = left - right
                    if values[0] == d or values[cut - 1] == d:
                        return True
                else:
                    d = right - left
                    if values[cut] == d or values[-1] == d:
                        return True
            return False

        if m == 1:
            return one_dim(grid[0])
        if n == 1:
            return one_dim([row[0] for row in grid])

        total = sum(map(sum, grid))

        def scan(lines, width: int) -> bool:
            left = 0
            a = Counter()
            b = Counter(x for line in lines for x in line)
            for cut in range(1, len(lines)):
                for x in lines[cut - 1]:
                    left += x; a[x] += 1; b[x] -= 1
                right = total - left
                if left == right:
                    return True
                if left > right:
                    d = left - right
                    # A one-row part can only delete either endpoint.
                    if (cut == 1 and (lines[0][0] == d or lines[0][-1] == d)) or (cut > 1 and a[d]):
                        return True
                else:
                    d = right - left
                    rows = len(lines) - cut
                    if (rows == 1 and (lines[-1][0] == d or lines[-1][-1] == d)) or (rows > 1 and b[d]):
                        return True
            return False

        return scan(grid, n) or scan(list(map(list, zip(*grid))), m)
