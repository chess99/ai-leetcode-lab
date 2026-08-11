# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:53:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        left=total=0; best=[float('inf')]*len(arr); answer=float('inf'); shortest=float('inf')
        for right,value in enumerate(arr):
            total+=value
            while total>target: total-=arr[left];left+=1
            if total==target:
                length=right-left+1
                if left: answer=min(answer,length+best[left-1])
                shortest=min(shortest,length)
            best[right]=shortest
        return answer if answer<float('inf') else -1
