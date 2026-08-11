# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:13:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp={};answer=0
        for word in sorted(words,key=len):
            dp[word]=1+max((dp.get(word[:i]+word[i+1:],0) for i in range(len(word))),default=0);answer=max(answer,dp[word])
        return answer
