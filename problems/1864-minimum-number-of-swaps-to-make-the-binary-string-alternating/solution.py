# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minSwaps(self, s: str) -> int:
        zeros=s.count('0');ones=len(s)-zeros
        if abs(zeros-ones)>1:return -1
        def swaps(first):return sum(c!=str((i+first)%2) for i,c in enumerate(s))//2
        if zeros>ones:return swaps(0)
        if ones>zeros:return swaps(1)
        return min(swaps(0),swaps(1))
