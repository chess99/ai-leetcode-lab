# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def minimumSubstringsInPartition(self, s: str) -> int:
  n=len(s); dp=[0]+[n]*n
  for i in range(n):
   cnt=[0]*26
   for j in range(i,n):
    cnt[ord(s[j])-97]+=1; vals=[x for x in cnt if x]
    if min(vals)==max(vals):dp[j+1]=min(dp[j+1],dp[i]+1)
  return dp[n]
