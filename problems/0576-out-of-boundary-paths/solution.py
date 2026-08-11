# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:24:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 1_000_000_007
        current = [[0] * n for _ in range(m)]
        current[startRow][startColumn] = 1
        escaped = 0

        for _ in range(maxMove):
            following = [[0] * n for _ in range(m)]
            for row in range(m):
                for column in range(n):
                    paths = current[row][column]
                    if paths == 0:
                        continue
                    for next_row, next_column in (
                        (row - 1, column),
                        (row + 1, column),
                        (row, column - 1),
                        (row, column + 1),
                    ):
                        if 0 <= next_row < m and 0 <= next_column < n:
                            following[next_row][next_column] = (
                                following[next_row][next_column] + paths
                            ) % modulo
                        else:
                            escaped = (escaped + paths) % modulo
            current = following
        return escaped
