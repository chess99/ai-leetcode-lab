# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numWays(self, s: str) -> int:
        ones = [i for i, char in enumerate(s) if char == '1']; mod = 10**9+7
        if not ones: return (len(s)-1)*(len(s)-2)//2 % mod
        if len(ones)%3: return 0
        part=len(ones)//3
        return (ones[part]-ones[part-1])*(ones[2*part]-ones[2*part-1])%mod
