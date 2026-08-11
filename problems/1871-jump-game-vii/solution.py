# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        reachable=[False]*len(s);reachable[0]=True;count=0
        for i in range(1,len(s)):
            if i-minJump>=0:count+=reachable[i-minJump]
            if i-maxJump-1>=0:count-=reachable[i-maxJump-1]
            reachable[i]=s[i]=='0' and count>0
        return reachable[-1]
