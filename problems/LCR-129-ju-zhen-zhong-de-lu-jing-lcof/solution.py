# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def wordPuzzle(self, grid: List[List[str]], target: str) -> bool:
        def dfs(r, c, i):
            if i == len(target): return True
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != target[i]: return False
            grid[r][c] = '#'
            ok = any(dfs(r + dr, c + dc, i + 1) for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)))
            grid[r][c] = target[i]
            return ok
        return any(dfs(r, c, 0) for r in range(len(grid)) for c in range(len(grid[0])))
