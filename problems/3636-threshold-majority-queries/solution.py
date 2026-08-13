# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
from math import isqrt
from typing import List


class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        values = sorted(set(nums))
        index = {value: i for i, value in enumerate(values)}
        encoded = [index[value] for value in nums]
        size = len(values)
        base = max(1, isqrt(len(nums)))
        ordered = sorted(enumerate(queries), key=lambda item: (item[1][0] // base, item[1][1] if (item[1][0] // base) % 2 == 0 else -item[1][1]))

        # Tree nodes store (largest frequency, smallest compressed value with it).
        leaf = 1
        while leaf < size:
            leaf <<= 1
        tree = [(0, size)] * (leaf * 2)
        count = [0] * size

        def set_count(position: int, frequency: int) -> None:
            node = leaf + position
            tree[node] = (frequency, position)
            node >>= 1
            while node:
                left, right = tree[node * 2], tree[node * 2 + 1]
                tree[node] = left if left[0] > right[0] or (left[0] == right[0] and left[1] < right[1]) else right
                node >>= 1

        def add(position: int, delta: int) -> None:
            value = encoded[position]
            count[value] += delta
            set_count(value, count[value])

        answer = [-1] * len(queries)
        left, right = 0, -1
        for query_index, (ql, qr, threshold) in ordered:
            while left > ql:
                left -= 1
                add(left, 1)
            while right < qr:
                right += 1
                add(right, 1)
            while left < ql:
                add(left, -1)
                left += 1
            while right > qr:
                add(right, -1)
                right -= 1
            frequency, value = tree[1]
            if frequency >= threshold:
                answer[query_index] = values[value]
        return answer
