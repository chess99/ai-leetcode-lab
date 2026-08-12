# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:50Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(map(str, board[0] + board[1]))
        target = '123450'
        neighbors = ((1, 3), (0, 2, 4), (1, 5),
                     (0, 4), (1, 3, 5), (2, 4))
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            state, moves = queue.popleft()
            if state == target:
                return moves
            zero = state.index('0')
            for following in neighbors[zero]:
                chars = list(state)
                chars[zero], chars[following] = chars[following], chars[zero]
                next_state = ''.join(chars)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, moves + 1))
        return -1
