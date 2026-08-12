# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:07Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        walls = set(map(tuple, blocked))
        limit = len(blocked) * (len(blocked) - 1) // 2

        def escapes(start, finish):
            queue = deque([tuple(start)])
            visited = {tuple(start)}
            while queue and len(visited) <= limit:
                row, column = queue.popleft()
                for next_row, next_column in ((row-1,column),(row+1,column),
                                              (row,column-1),(row,column+1)):
                    position = (next_row, next_column)
                    if (0 <= next_row < 10 ** 6 and 0 <= next_column < 10 ** 6
                            and position not in walls and position not in visited):
                        if position == tuple(finish):
                            return True
                        visited.add(position)
                        queue.append(position)
            return len(visited) > limit

        return escapes(source, target) and escapes(target, source)
