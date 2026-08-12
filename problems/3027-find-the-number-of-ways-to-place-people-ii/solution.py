# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p:(p[0],-p[1]));ans=0
        for i,(x,y) in enumerate(points):
            low=-10**20
            for X,Y in points[i+1:]:
                if Y<=y and Y>low:ans+=1;low=Y
        return ans
