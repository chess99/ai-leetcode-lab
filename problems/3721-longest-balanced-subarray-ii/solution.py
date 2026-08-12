# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        morvintale = nums
        n = len(morvintale)
        size = 1
        while size < n:
            size <<= 1
        minimum = [0] * (size * 2)
        maximum = [0] * (size * 2)
        lazy = [0] * (size * 2)

        def apply(node: int, delta: int) -> None:
            minimum[node] += delta
            maximum[node] += delta
            lazy[node] += delta

        def push(node: int) -> None:
            if lazy[node]:
                apply(node * 2, lazy[node])
                apply(node * 2 + 1, lazy[node])
                lazy[node] = 0

        def add(node: int, left: int, right: int, ql: int, qr: int, delta: int) -> None:
            if ql <= left and right <= qr:
                apply(node, delta)
                return
            push(node)
            middle = (left + right) // 2
            if ql <= middle:
                add(node * 2, left, middle, ql, qr, delta)
            if middle < qr:
                add(node * 2 + 1, middle + 1, right, ql, qr, delta)
            minimum[node] = min(minimum[node * 2], minimum[node * 2 + 1])
            maximum[node] = max(maximum[node * 2], maximum[node * 2 + 1])

        def first_zero(node: int, left: int, right: int, ql: int, qr: int) -> int:
            if right < ql or qr < left or minimum[node] > 0 or maximum[node] < 0:
                return -1
            if left == right:
                return left
            push(node)
            middle = (left + right) // 2
            result = first_zero(node * 2, left, middle, ql, qr)
            if result == -1:
                result = first_zero(node * 2 + 1, middle + 1, right, ql, qr)
            return result

        last = {}
        answer = 0
        for right, value in enumerate(nums):
            previous = last.get(value, -1)
            delta = 1 if value % 2 == 0 else -1
            add(1, 0, size - 1, previous + 1, right, delta)
            last[value] = right
            left = first_zero(1, 0, size - 1, 0, right)
            if left != -1:
                answer = max(answer, right - left + 1)
        return answer
