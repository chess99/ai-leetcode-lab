# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:21Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n=len(s)
        empty=[[False]*n for _ in range(n)]
        def adjacent(a,b):return (ord(a)-ord(b))%26 in (1,25)
        # Whether s[i..j] can be deleted completely.
        for length in range(2,n+1,2):
            for i in range(n-length+1):
                j=i+length-1
                for p in range(i+1,j+1,2):
                    if adjacent(s[i],s[p]) and (p==i+1 or empty[i+1][p-1]) and (p==j or empty[p+1][j]):
                        empty[i][j]=True;break
        best=['']*(n+1)
        for i in range(n-1,-1,-1):
            cur=s[i]+best[i+1]
            for p in range(i+1,n,2):
                if adjacent(s[i],s[p]) and (p==i+1 or empty[i+1][p-1]):
                    cur=min(cur,best[p+1])
            best[i]=cur
        return best[0]
