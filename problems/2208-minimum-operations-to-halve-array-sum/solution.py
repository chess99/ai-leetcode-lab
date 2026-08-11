# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:16Z
# Experiment: ai-leetcode-lab, round 1

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = [-float(value) for value in nums]
        heapify(heap)
        required_reduction = sum(nums) / 2
        reduction = 0.0
        operations = 0

        while reduction < required_reduction:
            value = -heappop(heap)
            halved = value / 2
            reduction += halved
            heappush(heap, -halved)
            operations += 1

        return operations
