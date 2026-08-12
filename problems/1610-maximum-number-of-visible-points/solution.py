# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:33Z
# Experiment: ai-leetcode-lab, round 1
from math import atan2,pi
from typing import List
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        same=0;directions=[]
        for x,y in points:
            if [x,y]==location:same+=1
            else:directions.append(atan2(y-location[1],x-location[0]))
        directions.sort();extended=directions+[value+2*pi for value in directions];width=angle*pi/180;left=best=0
        for right,value in enumerate(extended):
            while value-extended[left]>width+1e-12:left+=1
            if left<len(directions):best=max(best,min(len(directions),right-left+1))
        return same+best
