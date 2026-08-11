# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:19Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        heap=[(nums1[i]+nums2[0],i,0) for i in range(min(k,len(nums1)))]; heapq.heapify(heap); result=[]
        while heap and len(result)<k:
            _,i,j=heapq.heappop(heap); result.append([nums1[i],nums2[j]])
            if j+1<len(nums2): heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
        return result
