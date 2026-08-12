# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        from array import array

        rows, columns = len(plate), len(plate[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        state_count = rows * columns * 4
        unseen, unreachable = -2, -1
        distance = array('i', [unseen]) * state_count
        cap = num + 1

        def reaches(start_row: int, start_column: int,
                    start_direction: int) -> bool:
            row, column, direction = start_row, start_column, start_direction
            path_length = 0
            base_distance = unreachable

            while True:
                state = (row * columns + column) * 4 + direction
                known = distance[state]
                if known != unseen:
                    if known >= 0:
                        base_distance = known
                    break

                # A value below -2 marks a state on this traversal.  Meeting
                # one again means the deterministic path has entered a cycle.
                distance[state] = -3 - path_length
                path_length += 1

                dr, dc = directions[direction]
                next_row, next_column = row + dr, column + dc
                if not (0 <= next_row < rows and
                        0 <= next_column < columns):
                    break
                cell = plate[next_row][next_column]
                if cell == 'O':
                    base_distance = 0
                    break
                if cell == 'W':
                    direction = (direction - 1) % 4
                elif cell == 'E':
                    direction = (direction + 1) % 4
                row, column = next_row, next_column

            # Rewalk the newly visited prefix.  This avoids retaining a Python
            # list of as many as 4 * rows * columns integer objects.
            row, column, direction = start_row, start_column, start_direction
            remaining = path_length
            while remaining:
                state = (row * columns + column) * 4 + direction
                dr, dc = directions[direction]
                next_row, next_column = row + dr, column + dc
                cell = (plate[next_row][next_column]
                        if 0 <= next_row < rows and
                        0 <= next_column < columns else None)

                if base_distance < 0:
                    distance[state] = unreachable
                else:
                    distance[state] = min(cap, base_distance + remaining)

                if cell == 'W':
                    direction = (direction - 1) % 4
                elif cell == 'E':
                    direction = (direction + 1) % 4
                row, column = next_row, next_column
                remaining -= 1

            steps = distance[
                (start_row * columns + start_column) * 4 + start_direction
            ]
            return 0 <= steps <= num

        answer = []
        for column in range(1, columns - 1):
            if plate[0][column] == '.' and reaches(0, column, 2):
                answer.append([0, column])
            if rows > 1 and plate[rows - 1][column] == '.' and reaches(rows - 1, column, 0):
                answer.append([rows - 1, column])
        for row in range(1, rows - 1):
            if plate[row][0] == '.' and reaches(row, 0, 1):
                answer.append([row, 0])
            if columns > 1 and plate[row][columns - 1] == '.' and reaches(row, columns - 1, 3):
                answer.append([row, columns - 1])
        return answer
