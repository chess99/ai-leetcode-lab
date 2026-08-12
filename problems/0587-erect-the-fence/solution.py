# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        points = sorted(map(tuple, trees))
        def cross(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
        lower=[]
        for p in points:
            while len(lower)>1 and cross(lower[-2],lower[-1],p)<0: lower.pop()
            lower.append(p)
        upper=[]
        for p in reversed(points):
            while len(upper)>1 and cross(upper[-2],upper[-1],p)<0: upper.pop()
            upper.append(p)
        return [list(p) for p in set(lower+upper)]
