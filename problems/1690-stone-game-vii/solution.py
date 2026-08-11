# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp=[0]*len(stones);prefix=[0]
        for value in stones:prefix.append(prefix[-1]+value)
        for length in range(2,len(stones)+1):
            for left in range(len(stones)-length+1):
                right=left+length-1
                dp[left]=max(prefix[right+1]-prefix[left+1]-dp[left+1],prefix[right]-prefix[left]-dp[left])
        return dp[0]
