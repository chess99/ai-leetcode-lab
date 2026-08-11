# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr); left=0
        while left+1<n and arr[left]<=arr[left+1]: left+=1
        if left==n-1:return 0
        right=n-1
        while right and arr[right-1]<=arr[right]:right-=1
        answer=min(n-left-1,right); i=0
        for j in range(right,n):
            while i<=left and arr[i]<=arr[j]:i+=1
            answer=min(answer,j-i)
        return answer
