# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Revised by: Codex Desktop / gpt-5.6-sol / medium / sol-medium
# Created: 2026-08-12T17:58:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        times, rows, cols = len(maze), len(maze[0]), len(maze[0][0])
        cells = rows * cols
        target = cells - 1
        if target == 0:
            return True

        neighbors = []
        for cell in range(cells):
            r, c = divmod(cell, cols)
            current = [cell]
            if r:
                current.append(cell - cols)
            if r + 1 < rows:
                current.append(cell + cols)
            if c:
                current.append(cell - 1)
            if c + 1 < cols:
                current.append(cell + 1)
            neighbors.append(current)

        # Permanent scroll unused: positions reachable with temporary scroll
        # available / used. Permanent scroll used: for every current position,
        # an integer bitset records all possible permanently cleared cells.
        unused_available = 1
        unused_used = 0
        permanent_available = [0] * cells
        permanent_used = [0] * cells

        for time in range(1, times):
            open_cell = [maze[time][cell // cols][cell % cols] == "." for cell in range(cells)]
            next_unused_available = 0
            next_unused_used = 0
            next_permanent_available = [0] * cells
            next_permanent_used = [0] * cells

            for source in range(cells):
                source_bit = 1 << source
                ua = unused_available & source_bit
                uu = unused_used & source_bit
                pa = permanent_available[source]
                pu = permanent_used[source]
                if not (ua or uu or pa or pu):
                    continue

                for destination in neighbors[source]:
                    destination_bit = 1 << destination
                    if open_cell[destination]:
                        if ua:
                            next_unused_available |= destination_bit
                        if uu:
                            next_unused_used |= destination_bit
                        next_permanent_available[destination] |= pa
                        next_permanent_used[destination] |= pu
                    else:
                        # Use the temporary scroll for this one arrival.
                        if ua:
                            next_unused_used |= destination_bit
                        next_permanent_used[destination] |= pa
                        # An existing permanent scroll only opens its own cell.
                        next_permanent_available[destination] |= pa & destination_bit
                        next_permanent_used[destination] |= pu & destination_bit

                    # Use the permanent scroll on the destination. This is also
                    # allowed while that cell happens to be open at this time.
                    if ua:
                        next_permanent_available[destination] |= destination_bit
                    if uu:
                        next_permanent_used[destination] |= destination_bit

            unused_available, unused_used = next_unused_available, next_unused_used
            permanent_available, permanent_used = next_permanent_available, next_permanent_used
            if ((unused_available | unused_used) >> target) & 1:
                return True
            if permanent_available[target] or permanent_used[target]:
                return True
        return False
