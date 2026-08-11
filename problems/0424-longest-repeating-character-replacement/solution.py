# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={};left=best=most=0
        for right,c in enumerate(s):
            counts[c]=counts.get(c,0)+1;most=max(most,counts[c])
            while right-left+1-most>k:counts[s[left]]-=1;left+=1
            best=max(best,right-left+1)
        return best
