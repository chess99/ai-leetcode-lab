# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent={};first=second=None
        for edge in edges:
            u,v=edge
            if v in parent:first=parent[v];second=edge
            else:parent[v]=edge
        def cycle(skip):
            roots={}
            def find(x):
                roots.setdefault(x,x)
                if roots[x]!=x:roots[x]=find(roots[x])
                return roots[x]
            for edge in edges:
                if edge==skip:continue
                u,v=edge;fu,fv=find(u),find(v)
                if fu==fv:return edge
                roots[fv]=fu
        loop=cycle(second)
        return first if loop and first else second if second else loop
