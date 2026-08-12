# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        size = len(nums1)
        ones = [0] * (4 * size)
        lazy = [False] * (4 * size)

        def build(node, left, right):
            if left == right:
                ones[node] = nums1[left]
                return
            middle = (left + right) // 2
            build(node * 2, left, middle)
            build(node * 2 + 1, middle + 1, right)
            ones[node] = ones[node * 2] + ones[node * 2 + 1]

        def flip(node, left, right, query_left, query_right):
            if query_left <= left and right <= query_right:
                ones[node] = right - left + 1 - ones[node]
                lazy[node] = not lazy[node]
                return
            middle = (left + right) // 2
            if lazy[node]:
                for child, child_left, child_right in (
                    (node * 2, left, middle),
                    (node * 2 + 1, middle + 1, right),
                ):
                    ones[child] = child_right - child_left + 1 - ones[child]
                    lazy[child] = not lazy[child]
                lazy[node] = False
            if query_left <= middle:
                flip(node * 2, left, middle, query_left, query_right)
            if query_right > middle:
                flip(node * 2 + 1, middle + 1, right, query_left, query_right)
            ones[node] = ones[node * 2] + ones[node * 2 + 1]

        build(1, 0, size - 1)
        total = sum(nums2)
        answer = []
        for query_type, first, second in queries:
            if query_type == 1:
                flip(1, 0, size - 1, first, second)
            elif query_type == 2:
                total += first * ones[1]
            else:
                answer.append(total)
        return answer
