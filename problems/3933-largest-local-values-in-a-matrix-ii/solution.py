# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countLocalMaximums(self, matrix: list[list[int]]) -> int:
        tarmiqusve = matrix
        rows, columns = len(matrix), len(matrix[0])
        tree = [[0] * (columns + 1) for _ in range(rows + 1)]

        def add(row: int, column: int) -> None:
            i = row + 1
            while i <= rows:
                j = column + 1
                while j <= columns:
                    tree[i][j] += 1
                    j += j & -j
                i += i & -i

        def prefix(row: int, column: int) -> int:
            total = 0
            i = row
            while i > 0:
                j = column
                while j > 0:
                    total += tree[i][j]
                    j -= j & -j
                i -= i & -i
            return total

        def rectangle(r1: int, c1: int, r2: int, c2: int) -> int:
            return (prefix(r2 + 1, c2 + 1) - prefix(r1, c2 + 1)
                    - prefix(r2 + 1, c1) + prefix(r1, c1))

        cells = sorted(((matrix[r][c], r, c) for r in range(rows)
                        for c in range(columns) if matrix[r][c] > 0), reverse=True)
        answer = 0
        index = 0
        while index < len(cells):
            end = index
            value = cells[index][0]
            while end < len(cells) and cells[end][0] == value:
                end += 1

            for _, row, column in cells[index:end]:
                r1, r2 = max(0, row - value), min(rows - 1, row + value)
                c1, c2 = max(0, column - value), min(columns - 1, column + value)
                greater = rectangle(r1, c1, r2, c2)
                for rr in (row - value, row + value):
                    for cc in (column - value, column + value):
                        if 0 <= rr < rows and 0 <= cc < columns and matrix[rr][cc] > value:
                            greater -= 1
                if greater == 0:
                    answer += 1

            for _, row, column in cells[index:end]:
                add(row, column)
            index = end
        return answer
