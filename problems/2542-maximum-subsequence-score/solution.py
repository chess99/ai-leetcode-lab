# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap, total, answer = [], 0, 0
        for b, a in sorted(zip(nums2, nums1), reverse=True):
            heapq.heappush(heap, a)
            total += a
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                answer = max(answer, total * b)
        return answer
