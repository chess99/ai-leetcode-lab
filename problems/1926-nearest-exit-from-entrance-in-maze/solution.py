# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:05Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            row, col, distance = queue.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    if nr in (0, rows-1) or nc in (0, cols-1): return distance + 1
                    maze[nr][nc] = '+'; queue.append((nr,nc,distance+1))
        return -1
