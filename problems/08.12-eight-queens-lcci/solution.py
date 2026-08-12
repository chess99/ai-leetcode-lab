# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        columns = set()
        descending = set()
        ascending = set()
        placement = []

        def search(row: int) -> None:
            if row == n:
                answer.append(["." * column + "Q" + "." * (n - column - 1) for column in placement])
                return
            for column in range(n):
                if column in columns or row - column in descending or row + column in ascending:
                    continue
                columns.add(column)
                descending.add(row - column)
                ascending.add(row + column)
                placement.append(column)
                search(row + 1)
                placement.pop()
                columns.remove(column)
                descending.remove(row - column)
                ascending.remove(row + column)

        search(0)
        return answer
