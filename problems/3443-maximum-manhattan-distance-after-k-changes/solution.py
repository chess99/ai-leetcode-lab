# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans=0
        for a,b in (("N","E"),("N","W"),("S","E"),("S","W")):
            score=0
            for i,c in enumerate(s,1):
                score += 1 if c==a or c==b else -1
                ans=max(ans,min(i,score+2*k))
        return ans
