# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,right=0,len(arr)-1
        while left<right:
            mid=(left+right)//2
            if arr[mid]<arr[mid+1]: left=mid+1
            else: right=mid
        return left
