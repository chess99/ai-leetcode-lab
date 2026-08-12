# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs=sorted({x for x1,_,x2,_ in rectangles for x in (x1,x2)});area=0
        for left,right in zip(xs,xs[1:]):
            intervals=sorted((y1,y2) for x1,y1,x2,y2 in rectangles if x1<=left and right<=x2)
            covered=0;start=end=-1
            for low,high in intervals:
                if low>end:covered+=max(0,end-start);start,end=low,high
                else:end=max(end,high)
            covered+=max(0,end-start);area+=(right-left)*covered
        return area%1_000_000_007
