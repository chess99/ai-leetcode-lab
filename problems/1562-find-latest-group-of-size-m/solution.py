# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        lengths=[0]*(len(arr)+2);groups=0;answer=-1
        for step,position in enumerate(arr,1):
            left,right=lengths[position-1],lengths[position+1]
            if left==m:groups-=1
            if right==m:groups-=1
            length=left+right+1;lengths[position-left]=lengths[position+right]=length
            if length==m:groups+=1
            if groups:answer=step
        return answer
