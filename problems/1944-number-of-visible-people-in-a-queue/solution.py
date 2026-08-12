# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:01Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack=[];answer=[0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[i]>stack[-1]:stack.pop();answer[i]+=1
            if stack:answer[i]+=1
            stack.append(heights[i])
        return answer
