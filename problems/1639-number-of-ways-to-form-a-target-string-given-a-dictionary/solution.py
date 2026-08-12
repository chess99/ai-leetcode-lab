# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:35Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        counts=[Counter(word[column] for word in words) for column in range(len(words[0]))];dp=[0]*(len(target)+1);dp[0]=1;mod=1_000_000_007
        for count in counts:
            for i in range(len(target)-1,-1,-1):dp[i+1]=(dp[i+1]+dp[i]*count[target[i]])%mod
        return dp[-1]
