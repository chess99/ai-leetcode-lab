# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        def find_path() -> List[tuple[int, int]]:
            stack = [(0, 0)]
            parent = {(0, 0): None}
            while stack:
                r, c = stack.pop()
                if (r, c) == (rows - 1, cols - 1):
                    path = []
                    node = (r, c)
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return path
                for nr, nc in ((r + 1, c), (r, c + 1)):
                    if nr < rows and nc < cols and grid[nr][nc] and (nr, nc) not in parent:
                        parent[(nr, nc)] = (r, c)
                        stack.append((nr, nc))
            return []

        path = find_path()
        if not path:
            return True
        for r, c in path[1:-1]:
            grid[r][c] = 0
        return not find_path()
