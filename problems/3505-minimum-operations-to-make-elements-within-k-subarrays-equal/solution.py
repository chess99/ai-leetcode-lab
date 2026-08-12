# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:17Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        maritovexi = (nums, x, k)
        values = sorted(set(nums))
        size = len(values)
        count_bit = [0] * (size + 1)
        sum_bit = [0] * (size + 1)

        def add(value: int, delta: int) -> None:
            index = bisect_left(values, value) + 1
            while index <= size:
                count_bit[index] += delta
                sum_bit[index] += delta * value
                index += index & -index

        def prefix(bit: List[int], index: int) -> int:
            total = 0
            while index:
                total += bit[index]
                index -= index & -index
            return total

        def kth(order: int) -> int:
            index = 0
            step = 1 << (size.bit_length() - 1)
            while step:
                nxt = index + step
                if nxt <= size and count_bit[nxt] < order:
                    order -= count_bit[nxt]
                    index = nxt
                step >>= 1
            return index + 1

        for value in nums[:x]:
            add(value, 1)

        window_cost = []
        for left in range(len(nums) - x + 1):
            median_index = kth((x + 1) // 2)
            median = values[median_index - 1]
            left_count = prefix(count_bit, median_index)
            left_sum = prefix(sum_bit, median_index)
            total_sum = prefix(sum_bit, size)
            cost = (median * left_count - left_sum
                    + total_sum - left_sum - median * (x - left_count))
            window_cost.append(cost)
            if left + x < len(nums):
                add(nums[left], -1)
                add(nums[left + x], 1)

        n = len(nums)
        previous = [0] * (n + 1)
        infinity = 10 ** 30
        for _ in range(k):
            current = [infinity] * (n + 1)
            for length in range(1, n + 1):
                current[length] = current[length - 1]
                if length >= x and previous[length - x] < infinity:
                    current[length] = min(
                        current[length],
                        previous[length - x] + window_cost[length - x],
                    )
            previous = current
        return previous[n]
