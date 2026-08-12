# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque


class Solution:
    def bicycleYard(self, position: List[int], terrain: List[List[int]], obstacle: List[List[int]]) -> List[List[int]]:
        rows, columns = len(terrain), len(terrain[0])
        queue = deque([(position[0], position[1], 1)])
        visited = {(position[0], position[1], 1)}
        answer = set()
        while queue:
            row, column, speed = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if not (0 <= nr < rows and 0 <= nc < columns):
                    continue
                next_speed = speed + terrain[row][column] - terrain[nr][nc] - obstacle[nr][nc]
                state = (nr, nc, next_speed)
                if next_speed <= 0 or state in visited:
                    continue
                visited.add(state)
                queue.append(state)
                if next_speed == 1 and [nr, nc] != position:
                    answer.add((nr, nc))
        return [list(point) for point in sorted(answer)]
