# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:48Z
# Experiment: ai-leetcode-lab, round 1
import sys
from collections import deque
from typing import List


class Solution:
    def guardCastle(self, grid: List[str]) -> int:
        sys.setrecursionlimit(max(1000, len(grid[0]) * 8))
        columns = len(grid[0])
        cells = 2 * columns
        teleport = cells * 2
        source = teleport + 1
        sink = source + 1
        node_count = sink + 1
        graph = [[] for _ in range(node_count)]
        infinity = 10**8

        def add_edge(start: int, end: int, capacity: int) -> None:
            graph[start].append([end, capacity, len(graph[end])])
            graph[end].append([start, 0, len(graph[start]) - 1])

        def cell_id(row: int, column: int) -> int:
            return row * columns + column

        for row in range(2):
            for column in range(columns):
                kind = grid[row][column]
                if kind == "#":
                    continue
                cell = cell_id(row, column)
                inside, outside = cell * 2, cell * 2 + 1
                add_edge(inside, outside, 1 if kind == "." else infinity)
                if kind == "S":
                    add_edge(source, inside, infinity)
                elif kind == "C":
                    add_edge(outside, sink, infinity)
                elif kind == "P":
                    add_edge(outside, teleport, infinity)
                    add_edge(teleport, inside, infinity)
                for dr, dc in ((-1, 0), (0, -1)):
                    nr, nc = row + dr, column + dc
                    if nr < 0 or nc < 0 or grid[nr][nc] == "#":
                        continue
                    neighbor = cell_id(nr, nc)
                    add_edge(outside, neighbor * 2, infinity)
                    add_edge(neighbor * 2 + 1, inside, infinity)

        flow = 0
        while True:
            level = [-1] * node_count
            level[source] = 0
            queue = deque([source])
            while queue:
                node = queue.popleft()
                for neighbor, capacity, _ in graph[node]:
                    if capacity and level[neighbor] < 0:
                        level[neighbor] = level[node] + 1
                        queue.append(neighbor)
            if level[sink] < 0:
                break
            current = [0] * node_count

            def send(node: int, pushed: int) -> int:
                if node == sink:
                    return pushed
                while current[node] < len(graph[node]):
                    edge = graph[node][current[node]]
                    neighbor, capacity, reverse = edge
                    if capacity and level[neighbor] == level[node] + 1:
                        amount = send(neighbor, min(pushed, capacity))
                        if amount:
                            edge[1] -= amount
                            graph[neighbor][reverse][1] += amount
                            return amount
                    current[node] += 1
                return 0

            while True:
                pushed = send(source, infinity)
                if not pushed:
                    break
                flow += pushed
                if flow >= infinity:
                    return -1
        return flow
