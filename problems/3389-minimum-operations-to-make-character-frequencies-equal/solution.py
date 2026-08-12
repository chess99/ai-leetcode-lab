# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def makeStringGood(self, s: str) -> int:
        from collections import Counter
        cnt=Counter(s);freq=[cnt.get(chr(97+i),0)for i in range(26)];ans=len(s)
        for target in range(1,max(freq)+1):
            dp0=0;dp1=10**9
            for x in freq:
                nd0=min(dp0+x,dp1+x)
                nd1=min(dp0+abs(x-target),dp1+max(0,target-x))
                dp0,dp1=nd0,nd1
            ans=min(ans,dp0,dp1)
        return ans
