# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def challengeOfTheKeeper(self, maze: List[str]) -> int:
        n = len(maze)
        inf = 10**9
        target = start = (-1, -1)
        for i, row in enumerate(maze):
            for j, ch in enumerate(row):
                if ch == "S":
                    start = (i, j)
                elif ch == "T":
                    target = (i, j)

        # 卷轴释放后，从各位置到 T 的普通最短路。
        dist = [[inf] * n for _ in range(n)]
        tr, tc = target
        dist[tr][tc] = 0
        q = deque([target])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] != "#" and dist[nr][nc] == inf:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # danger[r][c] 是守护者在该空地释放卷轴时能造成的最坏结果。
        danger = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if maze[r][c] != ".":
                    continue
                worst = 0
                for nr, nc in ((n - 1 - r, c), (r, n - 1 - c)):
                    if maze[nr][nc] != "#":
                        worst = max(worst, dist[nr][nc])
                danger[r][c] = worst

        # 选择 S 到 T 的路径，使沿途所有可释放位置的 danger 最大值最小。
        best = [[inf] * n for _ in range(n)]
        sr, sc = start
        best[sr][sc] = 0
        heap = [(0, sr, sc)]
        while heap:
            value, r, c = heappop(heap)
            if value != best[r][c]:
                continue
            if (r, c) == target:
                return -1 if value >= inf else value
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < n) or maze[nr][nc] == "#":
                    continue
                nv = max(value, danger[nr][nc])
                if nv < best[nr][nc]:
                    best[nr][nc] = nv
                    heappush(heap, (nv, nr, nc))
        return -1
