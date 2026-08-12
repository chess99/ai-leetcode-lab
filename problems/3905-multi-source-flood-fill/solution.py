# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        import heapq

        lenqavirod = (n, m, sources)
        distance = [[10 ** 30] * m for _ in range(n)]
        grid = [[0] * m for _ in range(n)]
        queue = []
        for row, column, color in sources:
            distance[row][column] = 0
            grid[row][column] = color
            heapq.heappush(queue, (0, -color, row, column))

        while queue:
            steps, negative_color, row, column = heapq.heappop(queue)
            color = -negative_color
            if steps != distance[row][column] or color != grid[row][column]:
                continue
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                next_steps = steps + 1
                if next_steps < distance[nr][nc] or (next_steps == distance[nr][nc] and color > grid[nr][nc]):
                    distance[nr][nc] = next_steps
                    grid[nr][nc] = color
                    heapq.heappush(queue, (next_steps, -color, nr, nc))
        return grid
