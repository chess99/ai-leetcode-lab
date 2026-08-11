# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import defaultdict, deque

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        portals = defaultdict(list)
        for r, row in enumerate(matrix):
            for c, ch in enumerate(row):
                if ch.isupper(): portals[ch].append((r, c))
        q = deque([(0, 0, 0)])
        seen = {(0, 0)}
        used = set()
        while q:
            r, c, dist = q.popleft()
            if (r, c) == (m - 1, n - 1): return dist
            ch = matrix[r][c]
            if ch.isupper() and ch not in used:
                used.add(ch)
                for nr, nc in portals[ch]:
                    if (nr, nc) not in seen:
                        seen.add((nr, nc)); q.appendleft((nr, nc, dist))
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != '#' and (nr,nc) not in seen:
                    seen.add((nr,nc)); q.append((nr,nc,dist+1))
        return -1
