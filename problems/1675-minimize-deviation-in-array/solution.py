# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        import heapq
        heap=[];low=10**9
        for x in nums:
            if x % 2:
                x *= 2
            low=min(low,x);heapq.heappush(heap,-x)
        ans=10**9
        while True:
            x=-heapq.heappop(heap);ans=min(ans,x-low)
            if x%2:return ans
            x//=2;low=min(low,x);heapq.heappush(heap,-x)
