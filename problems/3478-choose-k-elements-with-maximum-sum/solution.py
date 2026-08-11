# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
import heapq
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        answer=[0]*len(nums1); heap=[]; total=0; order=sorted(range(len(nums1)),key=lambda i:nums1[i]); i=0
        while i<len(order):
            j=i
            while j<len(order) and nums1[order[j]]==nums1[order[i]]: answer[order[j]]=total; j+=1
            for t in range(i,j):
                value=nums2[order[t]]; heapq.heappush(heap,value); total+=value
                if len(heap)>k: total-=heapq.heappop(heap)
            i=j
        return answer
