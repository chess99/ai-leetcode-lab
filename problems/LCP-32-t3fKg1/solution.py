# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:46Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def processTasks(self, tasks: List[List[int]]) -> int:
        coordinates = sorted({point for start, end, _ in tasks for point in (start, end + 1)})
        segment_count = len(coordinates) - 1
        selected = [0] * (segment_count * 4 + 5)
        capacity = [0] * (segment_count * 4 + 5)
        full = [False] * (segment_count * 4 + 5)

        def build(node: int, left: int, right: int) -> None:
            if left == right:
                capacity[node] = coordinates[left + 1] - coordinates[left]
                return
            middle = (left + right) // 2
            build(node * 2, left, middle)
            build(node * 2 + 1, middle + 1, right)
            capacity[node] = capacity[node * 2] + capacity[node * 2 + 1]

        def push(node: int) -> None:
            if not full[node]:
                return
            for child in (node * 2, node * 2 + 1):
                selected[child] = capacity[child]
                full[child] = True
            full[node] = False

        def query(node: int, left: int, right: int, ql: int, qr: int) -> int:
            if ql <= left and right <= qr:
                return selected[node]
            push(node)
            middle = (left + right) // 2
            total = 0
            if ql <= middle:
                total += query(node * 2, left, middle, ql, qr)
            if qr > middle:
                total += query(node * 2 + 1, middle + 1, right, ql, qr)
            return total

        def fill_right(node: int, left: int, right: int, ql: int, qr: int, need: int) -> int:
            if need == 0 or right < ql or qr < left:
                return need
            free = capacity[node] - selected[node]
            if ql <= left and right <= qr and free <= need:
                selected[node] = capacity[node]
                full[node] = True
                return need - free
            if left == right:
                take = min(need, free)
                selected[node] += take
                full[node] = selected[node] == capacity[node]
                return need - take
            push(node)
            middle = (left + right) // 2
            need = fill_right(node * 2 + 1, middle + 1, right, ql, qr, need)
            need = fill_right(node * 2, left, middle, ql, qr, need)
            selected[node] = selected[node * 2] + selected[node * 2 + 1]
            return need

        build(1, 0, segment_count - 1)
        for start, end, period in sorted(tasks, key=lambda task: task[1]):
            left = bisect_left(coordinates, start)
            right = bisect_left(coordinates, end + 1) - 1
            need = period - query(1, 0, segment_count - 1, left, right)
            if need > 0:
                fill_right(1, 0, segment_count - 1, left, right, need)
        return selected[1]
