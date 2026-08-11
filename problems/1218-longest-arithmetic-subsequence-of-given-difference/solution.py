# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:28:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp={}; answer=0
        for value in arr:
            dp[value]=dp.get(value-difference,0)+1
            answer=max(answer,dp[value])
        return answer
