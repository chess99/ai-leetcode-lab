# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s=str(n);ans=0
        for l in range(1,len(s)):
            x=9
            for j in range(1,l):x*=10-j
            ans+=x
        used=set()
        for i,c in enumerate(s):
            for d in range(0 if i else 1,int(c)):
                if d not in used:
                    x=1
                    for j in range(i+1,len(s)):x*=10-j
                    ans+=x
            if int(c) in used:return ans
            used.add(int(c))
        return ans+1
