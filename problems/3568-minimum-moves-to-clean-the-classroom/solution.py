# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        trash, start = {}, None
        for r in range(m):
            for c, ch in enumerate(classroom[r]):
                if ch == 'L': trash[(r, c)] = len(trash)
                elif ch == 'S': start = (r, c)
        full = (1 << len(trash)) - 1
        q = deque([(start[0], start[1], 0, energy, 0)])
        best = {(start[0], start[1], 0): energy}
        while q:
            r, c, mask, power, dist = q.popleft()
            if mask == full: return dist
            if power == 0 and classroom[r][c] != 'R': continue
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n) or classroom[nr][nc] == 'X': continue
                nm = mask | (1 << trash[(nr,nc)] if (nr,nc) in trash else 0)
                np = energy if classroom[nr][nc] == 'R' else power - 1
                key = (nr, nc, nm)
                if np > best.get(key, -1):
                    best[key] = np; q.append((nr, nc, nm, np, dist + 1))
        return -1
