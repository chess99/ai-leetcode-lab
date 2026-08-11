# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:20Z
# Experiment: ai-leetcode-lab, round 1

import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates * 2 >= n:
            return sum(sorted(costs)[:k])

        left_heap = [(costs[index], index) for index in range(candidates)]
        right_heap = [
            (costs[index], index) for index in range(n - candidates, n)
        ]
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)
        left = candidates
        right = n - candidates - 1
        total = 0

        for _ in range(k):
            if left_heap[0] <= right_heap[0]:
                cost, _ = heapq.heappop(left_heap)
                total += cost
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1
            else:
                cost, _ = heapq.heappop(right_heap)
                total += cost
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1

        return total
