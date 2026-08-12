# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:03Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones=sum(arr)
        if not ones:return [0,2]
        if ones%3:return [-1,-1]
        kth=ones//3;starts=[];count=0
        for i,x in enumerate(arr):
            if x:
                count+=1
                if count in (1,kth+1,2*kth+1):starts.append(i)
        i,j,k=starts
        while k<len(arr):
            if arr[i]!=arr[j]or arr[j]!=arr[k]:return [-1,-1]
            i+=1;j+=1;k+=1
        return [i-1,j]
