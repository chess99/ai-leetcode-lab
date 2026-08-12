# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n=len(s);pal=[[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):pal[i][j]=s[i]==s[j]and(j-i<2 or pal[i+1][j-1])
        return any(pal[0][i]and pal[i+1][j]and pal[j+1][n-1]for i in range(n-2)for j in range(i+1,n-1))
