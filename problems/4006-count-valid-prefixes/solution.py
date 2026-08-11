# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:24:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        z=ans=0
        for i,c in enumerate(s,1):
            z+=c=='0';ans+=abs(2*z-i)<=1
        return ans
