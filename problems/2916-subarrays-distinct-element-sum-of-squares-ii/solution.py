# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        modulus = 10 ** 9 + 7
        size = len(nums)
        total = [0] * (4 * size)
        square = [0] * (4 * size)
        lazy = [0] * (4 * size)

        def apply(node, length, increment):
            square[node] += 2 * increment * total[node] + increment * increment * length
            total[node] += increment * length
            lazy[node] += increment

        def add(node, left, right, query_left, query_right):
            if query_left <= left and right <= query_right:
                apply(node, right - left + 1, 1)
                return
            middle = (left + right) // 2
            if lazy[node]:
                apply(node * 2, middle - left + 1, lazy[node])
                apply(node * 2 + 1, right - middle, lazy[node])
                lazy[node] = 0
            if query_left <= middle:
                add(node * 2, left, middle, query_left, query_right)
            if query_right > middle:
                add(node * 2 + 1, middle + 1, right, query_left, query_right)
            total[node] = total[node * 2] + total[node * 2 + 1]
            square[node] = square[node * 2] + square[node * 2 + 1]

        last = {}
        answer = 0
        for right, value in enumerate(nums):
            add(1, 0, size - 1, last.get(value, -1) + 1, right)
            last[value] = right
            answer = (answer + square[1]) % modulus
        return answer
