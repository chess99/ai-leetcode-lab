# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def minValidStrings(self, words: List[str], target: str) -> int:
  trie={}
  for w in words:
   p=trie
   for c in w:p=p.setdefault(c,{})
  n=len(target);dp=[0]+[n+1]*n
  for i in range(n):
   if dp[i]>n:continue
   p=trie
   for j in range(i,n):
    if target[j] not in p:break
    p=p[target[j]];dp[j+1]=min(dp[j+1],dp[i]+1)
  return dp[n] if dp[n]<=n else -1
