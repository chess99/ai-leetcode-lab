# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:11Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        third = len(nums) // 3
        left_sums = [0] * (2 * third)
        left_heap = []
        left_total = 0
        for index in range(2 * third):
            value = nums[index]
            heapq.heappush(left_heap, -value)
            left_total += value
            if len(left_heap) > third:
                left_total += heapq.heappop(left_heap)
            left_sums[index] = left_total

        right_heap = []
        right_total = 0
        answer = float("inf")
        for index in range(len(nums) - 1, third - 1, -1):
            value = nums[index]
            heapq.heappush(right_heap, value)
            right_total += value
            if len(right_heap) > third:
                right_total -= heapq.heappop(right_heap)
            if index <= 2 * third:
                answer = min(answer, left_sums[index - 1] - right_total)
        return answer
