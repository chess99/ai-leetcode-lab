# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:05:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips=[]
        for size in range(len(arr),1,-1):
            index=arr.index(size)
            if index==size-1: continue
            if index: arr[:index+1]=arr[:index+1][::-1];flips.append(index+1)
            arr[:size]=arr[:size][::-1];flips.append(size)
        return flips
