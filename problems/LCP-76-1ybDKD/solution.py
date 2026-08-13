# AI solution attribution
# Initially created by: Codex Desktop / gpt-5.6-terra / medium / terra-medium
# Completed by: Codex Desktop / gpt-5.6-sol / high / sol-high
# Experiment: ai-leetcode-lab, round 1
from itertools import product
from typing import List


class Solution:
    def getSchemeCount(self, n: int, m: int, chessboard: List[str]) -> int:
        # Keep the compressed dimension at most sqrt(30), hence at most five.
        if m > n:
            chessboard = ["".join(chessboard[i][j] for i in range(n)) for j in range(m)]
            n, m = m, n

        # A line only needs its last two occupied colours.  State 0 is empty,
        # 1/2 contain one B/R, and 3..6 contain the ordered last two colours.
        def advance(state: int, colour: int) -> int:
            if colour == 0:
                return state
            if state == 0:
                return colour
            if state <= 2:
                return 3 + (state - 1) * 2 + (colour - 1)
            older = (state - 3) // 2 + 1
            newer = (state - 3) % 2 + 1
            if colour != older:
                return -1
            return 3 + (newer - 1) * 2 + (colour - 1)

        allowed_rows = []
        for row in chessboard:
            choices = []
            for cell in row:
                choices.append((0,) if cell == "." else
                               (1,) if cell == "B" else
                               (2,) if cell == "R" else (0, 1, 2))
            valid = []
            for assignment in product(*choices):
                state = 0
                for colour in assignment:
                    state = advance(state, colour)
                    if state < 0:
                        break
                if state >= 0:
                    valid.append(assignment)
            allowed_rows.append(valid)

        dp = {(0,) * m: 1}
        for rows in allowed_rows:
            nxt = {}
            for states, ways in dp.items():
                for row in rows:
                    new_states = []
                    for state, colour in zip(states, row):
                        state = advance(state, colour)
                        if state < 0:
                            break
                        new_states.append(state)
                    else:
                        key = tuple(new_states)
                        nxt[key] = nxt.get(key, 0) + ways
            dp = nxt
        return sum(dp.values())
