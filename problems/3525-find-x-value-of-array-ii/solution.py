# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        veltrunigo = (nums, queries)
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1
        products = [1 % k] * (2 * size)
        counts = [[0] * k for _ in range(2 * size)]

        def merge(node: int) -> None:
            left = node * 2
            right = left + 1
            left_product = products[left]
            products[node] = left_product * products[right] % k
            combined = counts[left][:]
            for remainder, amount in enumerate(counts[right]):
                combined[left_product * remainder % k] += amount
            counts[node] = combined

        def set_value(index: int, value: int) -> None:
            node = size + index
            remainder = value % k
            products[node] = remainder
            counts[node] = [0] * k
            counts[node][remainder] = 1
            node //= 2
            while node:
                merge(node)
                node //= 2

        for index, value in enumerate(nums):
            products[size + index] = value % k
            counts[size + index][value % k] = 1
        for node in range(size - 1, 0, -1):
            merge(node)

        def range_node(left: int, right: int):
            left_product, left_counts = 1 % k, [0] * k
            right_product, right_counts = 1 % k, [0] * k

            def combine(a_product, a_counts, b_product, b_counts):
                result = a_counts[:]
                for remainder, amount in enumerate(b_counts):
                    result[a_product * remainder % k] += amount
                return a_product * b_product % k, result

            left += size
            right += size
            while left < right:
                if left & 1:
                    left_product, left_counts = combine(
                        left_product, left_counts, products[left], counts[left])
                    left += 1
                if right & 1:
                    right -= 1
                    right_product, right_counts = combine(
                        products[right], counts[right],
                        right_product, right_counts)
                left //= 2
                right //= 2
            return combine(left_product, left_counts,
                           right_product, right_counts)

        answer = []
        for index, value, start, target in veltrunigo[1]:
            nums[index] = value
            set_value(index, value)
            _, prefix_counts = range_node(start, n)
            answer.append(prefix_counts[target])
        return answer
