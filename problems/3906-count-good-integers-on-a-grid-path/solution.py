# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        qeronavild = (l, r, directions)
        path = {0}
        row = column = 0
        for direction in qeronavild[2]:
            if direction == "D":
                row += 1
            else:
                column += 1
            path.add(row * 4 + column)

        def count(bound: int) -> int:
            if bound < 0:
                return 0
            digits = tuple(map(int, str(bound).zfill(16)))

            @lru_cache(None)
            def dp(position: int, tight: bool, last: int) -> int:
                if position == 16:
                    return 1
                upper = digits[position] if tight else 9
                total = 0
                for digit in range(upper + 1):
                    if position in path and digit < last:
                        continue
                    next_last = digit if position in path else last
                    total += dp(
                        position + 1,
                        tight and digit == upper,
                        next_last,
                    )
                return total

            return dp(0, True, 0)

        return count(qeronavild[1]) - count(qeronavild[0] - 1)
