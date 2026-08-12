# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.rows = n
        self.seats = m
        self.remaining = [m] * n
        self.maximum = [0] * (4 * n)
        self.total = [0] * (4 * n)
        self.first_nonempty = 0

        def build(node, left, right):
            if left == right:
                self.maximum[node] = m
                self.total[node] = m
                return
            middle = (left + right) // 2
            build(node * 2, left, middle)
            build(node * 2 + 1, middle + 1, right)
            self.maximum[node] = m
            self.total[node] = self.total[node * 2] + self.total[node * 2 + 1]

        build(1, 0, n - 1)

    def _update(self, node, left, right, index):
        if left == right:
            self.maximum[node] = self.remaining[index]
            self.total[node] = self.remaining[index]
            return
        middle = (left + right) // 2
        if index <= middle:
            self._update(node * 2, left, middle, index)
        else:
            self._update(node * 2 + 1, middle + 1, right, index)
        self.maximum[node] = max(self.maximum[node * 2], self.maximum[node * 2 + 1])
        self.total[node] = self.total[node * 2] + self.total[node * 2 + 1]

    def _first_row(self, node, left, right, query_right, needed):
        if left > query_right or self.maximum[node] < needed:
            return -1
        if left == right:
            return left
        middle = (left + right) // 2
        result = self._first_row(node * 2, left, middle, query_right, needed)
        if result != -1:
            return result
        return self._first_row(node * 2 + 1, middle + 1, right, query_right, needed)

    def _prefix_total(self, node, left, right, query_right):
        if right <= query_right:
            return self.total[node]
        middle = (left + right) // 2
        result = self._prefix_total(node * 2, left, middle, query_right)
        if query_right > middle:
            result += self._prefix_total(node * 2 + 1, middle + 1, right, query_right)
        return result

    def gather(self, k: int, maxRow: int) -> List[int]:
        row = self._first_row(1, 0, self.rows - 1, maxRow, k)
        if row == -1:
            return []
        start = self.seats - self.remaining[row]
        self.remaining[row] -= k
        self._update(1, 0, self.rows - 1, row)
        if row == self.first_nonempty and self.remaining[row] == 0:
            while (self.first_nonempty < self.rows
                   and self.remaining[self.first_nonempty] == 0):
                self.first_nonempty += 1
        return [row, start]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self._prefix_total(1, 0, self.rows - 1, maxRow) < k:
            return False
        row = self.first_nonempty
        while k:
            take = min(k, self.remaining[row])
            self.remaining[row] -= take
            k -= take
            self._update(1, 0, self.rows - 1, row)
            if self.remaining[row] == 0:
                row += 1
        self.first_nonempty = row
        return True


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
