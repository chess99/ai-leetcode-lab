# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i,j,d):
            if i==len(s1) and j==len(s2):return d==0
            if i<len(s1) and s1[i].isdigit():
                x=0
                for p in range(i,min(i+3,len(s1))):
                    if not s1[p].isdigit():break
                    x=x*10+int(s1[p])
                    if dfs(p+1,j,d+x):return True
            if j<len(s2) and s2[j].isdigit():
                x=0
                for p in range(j,min(j+3,len(s2))):
                    if not s2[p].isdigit():break
                    x=x*10+int(s2[p])
                    if dfs(i,p+1,d-x):return True
            if d>0:return j<len(s2) and not s2[j].isdigit() and dfs(i,j+1,d-1)
            if d<0:return i<len(s1) and not s1[i].isdigit() and dfs(i+1,j,d+1)
            return i<len(s1) and j<len(s2) and not s1[i].isdigit() and not s2[j].isdigit() and s1[i]==s2[j] and dfs(i+1,j+1,0)
        return dfs(0,0,0)
