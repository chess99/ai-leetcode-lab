# AI solution attribution
# Original creator: Codex Desktop / gpt-5.6-terra / medium / terra-medium
# Solver: Codex Desktop / gpt-5.6-sol / ultra / sol-ultra
# Experiment: ai-leetcode-lab, profile escalation
from heapq import heappop, heappush
from typing import List


class Solution:
    def reservoir(self, shape: List[str]) -> int:
        rows, cols = len(shape), len(shape[0])
        graph = []
        bottom = []
        area = []
        side = {}

        def add_region(r: int, c: int, sides, is_square: bool) -> None:
            node = len(graph)
            graph.append([])
            bottom.append(rows - 1 - r)
            area.append(2 if is_square else 1)
            for name in sides:
                side[r, c, name] = node

        # A diagonal cuts its cell into two open triangular regions.  A dot is
        # one square region.  Areas are measured in half-cell units.
        for r, row in enumerate(shape):
            for c, ch in enumerate(row):
                if ch == '.':
                    add_region(r, c, "TRBL", True)
                elif ch == 'l':              # top-left to bottom-right
                    add_region(r, c, "TR", False)
                    add_region(r, c, "BL", False)
                else:                         # bottom-left to top-right
                    add_region(r, c, "TL", False)
                    add_region(r, c, "BR", False)

        def connect(a: int, b: int, height: int) -> None:
            graph[a].append((b, height))
            graph[b].append((a, height))

        outside = []
        for r in range(rows):
            y = rows - 1 - r
            for c in range(cols):
                if c:
                    connect(side[r, c, 'L'], side[r, c - 1, 'R'], y)
                else:
                    outside.append((side[r, c, 'L'], y))
                if c == cols - 1:
                    outside.append((side[r, c, 'R'], y))

                if r:
                    connect(side[r, c, 'T'], side[r - 1, c, 'B'], y + 1)
                else:
                    outside.append((side[r, c, 'T'], rows))
                if r == rows - 1:
                    outside.append((side[r, c, 'B'], 0))

        # escape[v] is the least possible maximum portal height on any path
        # from region v to the exterior (a minimax multi-source Dijkstra).
        infinity = rows + 1
        escape = [infinity] * len(graph)
        heap = []
        for node, height in outside:
            if height < escape[node]:
                escape[node] = height
                heappush(heap, (height, node))

        while heap:
            value, node = heappop(heap)
            if value != escape[node]:
                continue
            for nxt, portal in graph[node]:
                candidate = max(value, portal)
                if candidate < escape[nxt]:
                    escape[nxt] = candidate
                    heappush(heap, (candidate, nxt))

        answer = 0
        for node in range(len(graph)):
            # infinity means an initially sealed (dry) region.  Otherwise a
            # region keeps its full cell-height water exactly when no escape
            # path stays below its top edge.
            if escape[node] != infinity and escape[node] >= bottom[node] + 1:
                answer += area[node]
        return answer
