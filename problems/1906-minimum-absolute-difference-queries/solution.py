# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:47:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[[0]*101]
        for value in nums:
            current=prefix[-1].copy();current[value]+=1;prefix.append(current)
        answer=[]
        for left,right in queries:
            previous=None;best=101
            for value in range(1,101):
                if prefix[right+1][value]>prefix[left][value]:
                    if previous is not None:best=min(best,value-previous)
                    previous=value
            answer.append(-1 if best==101 else best)
        return answer
