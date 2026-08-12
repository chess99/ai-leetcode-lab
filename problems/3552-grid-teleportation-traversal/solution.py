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
        inf = m * n + 1
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        used = set()
        while q:
            r, c = q.popleft()
            current = dist[r][c]
            ch = matrix[r][c]
            if ch.isupper() and ch not in used:
                used.add(ch)
                for nr, nc in portals[ch]:
                    if current < dist[nr][nc]:
                        dist[nr][nc] = current
                        q.appendleft((nr, nc))
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != '#'
                        and current + 1 < dist[nr][nc]):
                    dist[nr][nc] = current + 1
                    q.append((nr,nc))
        answer = dist[m - 1][n - 1]
        return answer if answer < inf else -1
