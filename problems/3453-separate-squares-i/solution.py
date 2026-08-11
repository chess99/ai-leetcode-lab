# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total=sum(side*side for _,_,side in squares); lo=min(y for _,y,_ in squares); hi=max(y+side for _,y,side in squares)
        for _ in range(60):
            mid=(lo+hi)/2; below=sum(side*min(side,max(0,mid-y)) for _,y,side in squares)
            if below*2>=total: hi=mid
            else: lo=mid
        return hi
