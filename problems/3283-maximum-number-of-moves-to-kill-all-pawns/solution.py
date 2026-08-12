# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:32Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from functools import lru_cache
from typing import List


class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        points = positions + [[kx, ky]]
        pawn_count = len(positions)
        distances = [[0] * len(points) for _ in points]
        moves = ((1, 2), (1, -2), (-1, 2), (-1, -2),
                 (2, 1), (2, -1), (-2, 1), (-2, -1))
        for source, (x, y) in enumerate(points):
            board = [[-1] * 50 for _ in range(50)]
            board[x][y] = 0
            queue = deque([(x, y)])
            while queue:
                a, b = queue.popleft()
                for da, db in moves:
                    na, nb = a + da, b + db
                    if 0 <= na < 50 and 0 <= nb < 50 and board[na][nb] == -1:
                        board[na][nb] = board[a][b] + 1
                        queue.append((na, nb))
            for target, (a, b) in enumerate(points):
                distances[source][target] = board[a][b]

        @lru_cache(None)
        def game(mask, current):
            if mask == (1 << pawn_count) - 1:
                return 0
            values = [distances[current][following]
                      + game(mask | 1 << following, following)
                      for following in range(pawn_count)
                      if mask >> following & 1 == 0]
            return (max(values) if mask.bit_count() % 2 == 0 else min(values))

        return game(0, pawn_count)
