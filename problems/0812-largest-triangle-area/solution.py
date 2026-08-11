# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:04:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        best=0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                    a,b,c=points[i],points[j],points[k]
                    best=max(best,abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))/2)
        return best
