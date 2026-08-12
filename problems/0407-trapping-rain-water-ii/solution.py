# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:15Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        rows, columns = len(heightMap), len(heightMap[0])
        if rows < 3 or columns < 3:
            return 0
        heap, visited = [], [[False] * columns for _ in range(rows)]
        for row in range(rows):
            for column in (0, columns - 1):
                if not visited[row][column]:
                    visited[row][column] = True
                    heapq.heappush(heap, (heightMap[row][column], row, column))
        for column in range(columns):
            for row in (0, rows - 1):
                if not visited[row][column]:
                    visited[row][column] = True
                    heapq.heappush(heap, (heightMap[row][column], row, column))
        answer = 0
        while heap:
            boundary, row, column = heapq.heappop(heap)
            for next_row, next_column in ((row-1,column),(row+1,column),(row,column-1),(row,column+1)):
                if 0 <= next_row < rows and 0 <= next_column < columns and not visited[next_row][next_column]:
                    visited[next_row][next_column] = True
                    height = heightMap[next_row][next_column]
                    answer += max(0, boundary - height)
                    heapq.heappush(heap, (max(boundary, height), next_row, next_column))
        return answer
