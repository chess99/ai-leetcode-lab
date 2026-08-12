# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:17Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small, large = [], []
        delayed = defaultdict(int)
        small_size = large_size = 0

        def prune(heap):
            while heap:
                value = -heap[0] if heap is small else heap[0]
                if not delayed[value]:
                    break
                delayed[value] -= 1
                heapq.heappop(heap)

        def balance():
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                heapq.heappush(large, -heapq.heappop(small))
                small_size -= 1
                large_size += 1
                prune(small)
            elif small_size < large_size:
                heapq.heappush(small, -heapq.heappop(large))
                small_size += 1
                large_size -= 1
                prune(large)

        def add(value):
            nonlocal small_size, large_size
            if not small or value <= -small[0]:
                heapq.heappush(small, -value)
                small_size += 1
            else:
                heapq.heappush(large, value)
                large_size += 1
            balance()

        def remove(value):
            nonlocal small_size, large_size
            delayed[value] += 1
            if value <= -small[0]:
                small_size -= 1
                if value == -small[0]:
                    prune(small)
            else:
                large_size -= 1
                if large and value == large[0]:
                    prune(large)
            balance()

        for value in nums[:k]:
            add(value)
        answer = []
        for right in range(k, len(nums) + 1):
            answer.append(float(-small[0]) if k % 2
                          else (-small[0] + large[0]) / 2.0)
            if right < len(nums):
                remove(nums[right - k])
                add(nums[right])
        return answer
