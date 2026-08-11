# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import heapq

        heapq.heapify(nums)
        operations = 0
        while nums[0] < k:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            heapq.heappush(nums, first * 2 + second)
            operations += 1
        return operations
