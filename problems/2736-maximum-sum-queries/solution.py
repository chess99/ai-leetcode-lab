# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:40Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        points = sorted(zip(nums1, nums2), reverse=True)
        ordered_queries = sorted(((x, y, index) for index, (x, y) in enumerate(queries)),
                                 reverse=True)
        ys = sorted(set(nums2))
        size = len(ys)
        tree = [-1] * (size + 1)

        def update(index, value):
            index = size - index
            while index <= size:
                tree[index] = max(tree[index], value)
                index += index & -index

        def query(index):
            index = size - index
            answer = -1
            while index:
                answer = max(answer, tree[index])
                index -= index & -index
            return answer

        answer = [-1] * len(queries)
        point = 0
        for minimum_x, minimum_y, index in ordered_queries:
            while point < len(points) and points[point][0] >= minimum_x:
                first, second = points[point]
                update(bisect_left(ys, second), first + second)
                point += 1
            position = bisect_left(ys, minimum_y)
            if position < size:
                answer[index] = query(position)
        return answer
