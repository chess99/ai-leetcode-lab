# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        ordered = sorted(queries)
        heap = []
        ending = [0] * (len(nums) + 1)
        selected = active = index = 0
        for position, need in enumerate(nums):
            active -= ending[position]
            while index < len(ordered) and ordered[index][0] <= position:
                heapq.heappush(heap, -ordered[index][1])
                index += 1
            while heap and -heap[0] < position:
                heapq.heappop(heap)
            while active < need:
                # Valid intervals are popped first by their farthest right end.
                # After those are consumed, an expired interval can surface.
                if not heap or -heap[0] < position:
                    return -1
                right = -heapq.heappop(heap)
                selected += 1
                active += 1
                ending[right + 1] += 1
        return len(queries) - selected
