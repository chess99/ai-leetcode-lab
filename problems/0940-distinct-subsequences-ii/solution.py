# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod=10**9+7;total=1;last={}
        for c in s:
            old=total;total=(2*total-last.get(c,0))%mod;last[c]=old
        return(total-1)%mod
