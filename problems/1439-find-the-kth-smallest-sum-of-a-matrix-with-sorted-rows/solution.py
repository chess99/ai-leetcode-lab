# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:55Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        sums = [0]
        for row in mat:
            heap = [(sums[0] + row[0], 0, 0)]
            merged = []
            while heap and len(merged) < k:
                value, sum_index, row_index = heapq.heappop(heap)
                merged.append(value)
                if row_index + 1 < len(row):
                    heapq.heappush(heap, (sums[sum_index] + row[row_index + 1],
                                          sum_index, row_index + 1))
                if row_index == 0 and sum_index + 1 < len(sums):
                    heapq.heappush(heap, (sums[sum_index + 1] + row[0],
                                          sum_index + 1, 0))
            sums = merged
        return sums[k - 1]
