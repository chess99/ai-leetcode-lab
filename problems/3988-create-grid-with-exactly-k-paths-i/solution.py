# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        seravolith = (m, n, k)
        def count(grid):
            dp = [0] * n
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == '#':
                        dp[j] = 0
                    elif i == 0 and j == 0:
                        dp[j] = 1
                    else:
                        dp[j] += dp[j - 1] if j else 0
            return dp[-1]

        # Two open horizontal lanes have one path for every usable vertical edge.
        if m >= 2 and n >= k:
            grid = [['#'] * n for _ in range(m)]
            for j in range(k):
                grid[0][j] = '.'
            for j in range(n):
                grid[1][j] = '.'
            for i in range(2, m):
                grid[i][-1] = '.'
            return [''.join(row) for row in grid]
        if n >= 2 and m >= k:
            grid = [['#'] * n for _ in range(m)]
            for i in range(k):
                grid[i][0] = '.'
            for i in range(m):
                grid[i][1] = '.'
            for j in range(2, n):
                grid[-1][j] = '.'
            return [''.join(row) for row in grid]

        # The only remaining dimensions are at most 3 in both directions.
        grid = [['.'] * n for _ in range(m)]
        cells = [(i, j) for i in range(m) for j in range(n)
                 if (i, j) not in ((0, 0), (m - 1, n - 1))]
        for mask in range(1 << len(cells)):
            for bit, (i, j) in enumerate(cells):
                grid[i][j] = '#' if mask >> bit & 1 else '.'
            if count(grid) == k:
                return [''.join(row) for row in grid]
        return []
