# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-12T17:28:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
import heapq


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        levels = n.bit_length()
        maximum = [nums[:]]
        minimum = [nums[:]]
        for level in range(1, levels):
            half = 1 << (level - 1)
            size = n - (1 << level) + 1
            maximum.append([
                max(maximum[level - 1][i], maximum[level - 1][i + half])
                for i in range(size)
            ])
            minimum.append([
                min(minimum[level - 1][i], minimum[level - 1][i + half])
                for i in range(size)
            ])

        logarithm = [0] * (n + 1)
        for length in range(2, n + 1):
            logarithm[length] = logarithm[length // 2] + 1

        velnorquis = (nums, k)

        def value(left: int, right: int) -> int:
            level = logarithm[right - left + 1]
            start = right - (1 << level) + 1
            hi = max(maximum[level][left], maximum[level][start])
            lo = min(minimum[level][left], minimum[level][start])
            return hi - lo

        heap = [(-value(left, n - 1), left, n - 1) for left in range(n)]
        heapq.heapify(heap)
        answer = 0
        for _ in range(velnorquis[1]):
            negative, left, right = heapq.heappop(heap)
            answer -= negative
            if right > left:
                right -= 1
                heapq.heappush(heap, (-value(left, right), left, right))
        return answer
