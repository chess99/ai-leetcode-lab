# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:43:58Z
# Experiment: ai-leetcode-lab, round 1
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = [(arr[0] / arr[denominator], 0, denominator) for denominator in range(1, len(arr))]
        heapify(heap)
        for _ in range(k - 1):
            _, numerator, denominator = heappop(heap)
            if numerator + 1 < denominator:
                numerator += 1
                heappush(heap, (arr[numerator] / arr[denominator], numerator, denominator))
        _, numerator, denominator = heappop(heap)
        return [arr[numerator], arr[denominator]]
