# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        colors={value for row in targetGrid for value in row};bounds={color:[len(targetGrid),len(targetGrid[0]),-1,-1] for color in colors}
        for r,row in enumerate(targetGrid):
            for c,color in enumerate(row):
                b=bounds[color];b[0]=min(b[0],r);b[1]=min(b[1],c);b[2]=max(b[2],r);b[3]=max(b[3],c)
        graph={color:set() for color in colors};indegree={color:0 for color in colors}
        for color,(r1,c1,r2,c2) in bounds.items():
            for r in range(r1,r2+1):
                for c in range(c1,c2+1):
                    other=targetGrid[r][c]
                    if other!=color and other not in graph[color]:graph[color].add(other);indegree[other]+=1
        stack=[color for color in colors if indegree[color]==0];seen=0
        while stack:
            color=stack.pop();seen+=1
            for other in graph[color]:
                indegree[other]-=1
                if indegree[other]==0:stack.append(other)
        return seen==len(colors)
