# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:16:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        negative_infinity = -10 ** 30

        def leaf(value):
            return (0, negative_infinity, negative_infinity, value)

        def merge(left, right):
            result = [negative_infinity] * 4
            for left_endpoint in range(2):
                for right_endpoint in range(2):
                    result[left_endpoint * 2 + right_endpoint] = max(
                        left[left_endpoint * 2] + right[right_endpoint],
                        left[left_endpoint * 2] + right[2 + right_endpoint],
                        left[left_endpoint * 2 + 1] + right[right_endpoint],
                    )
            return tuple(result)

        size = 1
        while size < len(nums):
            size <<= 1
        tree = [leaf(negative_infinity)] * (2 * size)
        for index, value in enumerate(nums):
            tree[size + index] = leaf(value)
        for index in range(size - 1, 0, -1):
            tree[index] = merge(tree[index << 1], tree[index << 1 | 1])

        answer = 0
        modulus = 1_000_000_007
        for position, value in queries:
            index = size + position
            tree[index] = leaf(value)
            index >>= 1
            while index:
                tree[index] = merge(tree[index << 1], tree[index << 1 | 1])
                index >>= 1
            answer = (answer + max(0, *tree[1])) % modulus
        return answer
