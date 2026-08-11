# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def maxScore(self, a: List[int], b: List[int]) -> int:
  dp=[-10**30]*5;dp[0]=0
  for x in b:
   for i in range(3,-1,-1):dp[i+1]=max(dp[i+1],dp[i]+a[i]*x)
  return dp[4]
