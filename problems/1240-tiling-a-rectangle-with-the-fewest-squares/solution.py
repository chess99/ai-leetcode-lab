# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n>m:n,m=m,n
        best=n*m
        def dfs(heights,used):
            nonlocal best
            if used>=best:return
            low=min(heights)
            if low==n:best=used;return
            start=heights.index(low);end=start
            while end<m and heights[end]==low:end+=1
            for side in range(min(n-low,end-start),0,-1):dfs(heights[:start]+tuple(x+side for x in heights[start:start+side])+heights[start+side:],used+1)
        dfs((0,)*m,0);return best
