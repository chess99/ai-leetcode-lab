# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:02Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        tails=[];answer=[]
        for value in obstacles:
            index=bisect_right(tails,value)
            if index==len(tails):tails.append(value)
            else:tails[index]=value
            answer.append(index+1)
        return answer
