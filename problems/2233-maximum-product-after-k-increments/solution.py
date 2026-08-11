# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:18Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        modulo = 10**9 + 7
        heap = nums[:]
        heapq.heapify(heap)

        for _ in range(k):
            smallest = heapq.heappop(heap)
            heapq.heappush(heap, smallest + 1)

        product = 1
        for number in heap:
            product = product * number % modulo

        return product
