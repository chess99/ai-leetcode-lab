# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:02Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        size=row*col;parent=list(range(size+2));top=size;bottom=size+1;land=set()
        def find(x):
            while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
            return x
        def union(a,b):parent[find(a)]=find(b)
        for day in range(len(cells)-1,-1,-1):
            r,c=cells[day][0]-1,cells[day][1]-1;index=r*col+c;land.add(index)
            if r==0:union(index,top)
            if r==row-1:union(index,bottom)
            for rr,cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                following=rr*col+cc
                if 0<=rr<row and 0<=cc<col and following in land:union(index,following)
            if find(top)==find(bottom):return day
