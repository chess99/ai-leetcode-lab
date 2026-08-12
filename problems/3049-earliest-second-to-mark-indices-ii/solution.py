# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        import heapq

        size = len(nums)
        ordinary_work = sum(nums) + size

        def feasible(seconds):
            first = [-1] * size
            for time in range(seconds):
                index = changeIndices[time] - 1
                if first[index] == -1:
                    first[index] = time

            selected = []
            saved_decrements = 0
            free = 0
            for time in range(seconds - 1, -1, -1):
                index = changeIndices[time] - 1
                if time == first[index] and nums[index] > 1:
                    heapq.heappush(selected, nums[index])
                    saved_decrements += nums[index]
                    if free:
                        free -= 1
                    else:
                        removed = heapq.heappop(selected)
                        saved_decrements -= removed
                        free += 1
                else:
                    free += 1

            remaining_work = ordinary_work - saved_decrements - len(selected)
            return free >= remaining_work

        low = 1
        high = len(changeIndices)
        while low < high:
            middle = (low + high) // 2
            if feasible(middle):
                high = middle
            else:
                low = middle + 1
        return low if feasible(low) else -1
