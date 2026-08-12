# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def ok(x):
            need=0;i=0
            while i<len(s):
                j=i
                while j<len(s) and s[j]==s[i]:j+=1
                need+=(j-i)//(x+1);i=j
            return need<=numOps
        a=sum(s[i]==str(i%2) for i in range(len(s)));b=len(s)-a
        if min(a,b)<=numOps:return 1
        lo,hi=2,len(s)
        while lo<hi:
            mid=(lo+hi)//2
            if ok(mid):hi=mid
            else:lo=mid+1
        return lo
