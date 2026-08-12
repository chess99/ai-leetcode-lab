# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:44Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        infinity = 10 ** 15
        maximum_wait = 10 ** 9
        fire_time = [[infinity] * columns for _ in range(rows)]
        queue = deque()
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    fire_time[row][column] = 0
                    queue.append((row, column))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            row, column = queue.popleft()
            for row_step, column_step in directions:
                next_row = row + row_step
                next_column = column + column_step
                if (0 <= next_row < rows and 0 <= next_column < columns
                        and grid[next_row][next_column] != 2
                        and fire_time[next_row][next_column] == infinity):
                    fire_time[next_row][next_column] = fire_time[row][column] + 1
                    queue.append((next_row, next_column))

        destination = (rows - 1, columns - 1)

        def can_escape(wait):
            if wait >= fire_time[0][0]:
                return False
            seen = [[False] * columns for _ in range(rows)]
            seen[0][0] = True
            queue = deque([(0, 0, wait)])
            while queue:
                row, column, time = queue.popleft()
                for row_step, column_step in directions:
                    next_row = row + row_step
                    next_column = column + column_step
                    if not (0 <= next_row < rows and 0 <= next_column < columns):
                        continue
                    if grid[next_row][next_column] == 2 or seen[next_row][next_column]:
                        continue
                    arrival = time + 1
                    if (next_row, next_column) == destination:
                        if arrival <= fire_time[next_row][next_column]:
                            return True
                    elif arrival < fire_time[next_row][next_column]:
                        seen[next_row][next_column] = True
                        queue.append((next_row, next_column, arrival))
            return destination == (0, 0)

        if not can_escape(0):
            return -1
        if can_escape(maximum_wait):
            return maximum_wait
        low = 0
        high = maximum_wait - 1
        while low < high:
            middle = (low + high + 1) // 2
            if can_escape(middle):
                low = middle
            else:
                high = middle - 1
        return low
