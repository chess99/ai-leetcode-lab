# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:44Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        rows, columns = len(maze), len(maze[0])
        mechanisms = []
        stones = []
        start = target = None
        for row in range(rows):
            for column in range(columns):
                cell = maze[row][column]
                if cell == 'M':
                    mechanisms.append((row, column))
                elif cell == 'O':
                    stones.append((row, column))
                elif cell == 'S':
                    start = (row, column)
                elif cell == 'T':
                    target = (row, column)

        def bfs(origin):
            distance = [[-1] * columns for _ in range(rows)]
            distance[origin[0]][origin[1]] = 0
            queue = deque([origin])
            while queue:
                row, column = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, column + dc
                    if (0 <= nr < rows and 0 <= nc < columns and
                            maze[nr][nc] != '#' and distance[nr][nc] == -1):
                        distance[nr][nc] = distance[row][column] + 1
                        queue.append((nr, nc))
            return distance

        start_distance = bfs(start)
        if not mechanisms:
            return start_distance[target[0]][target[1]]
        distances = [bfs(mechanism) for mechanism in mechanisms]
        count = len(mechanisms)
        start_cost = [10 ** 9] * count
        transition = [[10 ** 9] * count for _ in range(count)]
        finish = [0] * count
        for i, (row, column) in enumerate(mechanisms):
            finish[i] = distances[i][target[0]][target[1]]
            for stone_row, stone_column in stones:
                a = start_distance[stone_row][stone_column]
                b = distances[i][stone_row][stone_column]
                if a >= 0 and b >= 0:
                    start_cost[i] = min(start_cost[i], a + b)
            for j in range(i):
                for stone_row, stone_column in stones:
                    a = distances[i][stone_row][stone_column]
                    b = distances[j][stone_row][stone_column]
                    if a >= 0 and b >= 0:
                        transition[i][j] = transition[j][i] = min(
                            transition[i][j], a + b)
        if any(cost == 10 ** 9 for cost in start_cost) or any(x < 0 for x in finish):
            return -1
        full = 1 << count
        infinity = 10 ** 9
        dp = [[infinity] * count for _ in range(full)]
        for i in range(count):
            dp[1 << i][i] = start_cost[i]
        for mask in range(full):
            for last in range(count):
                if dp[mask][last] == infinity:
                    continue
                for nxt in range(count):
                    if mask >> nxt & 1 or transition[last][nxt] == infinity:
                        continue
                    dp[mask | (1 << nxt)][nxt] = min(
                        dp[mask | (1 << nxt)][nxt],
                        dp[mask][last] + transition[last][nxt])
        answer = min(dp[-1][last] + finish[last] for last in range(count))
        return -1 if answer >= infinity else answer
