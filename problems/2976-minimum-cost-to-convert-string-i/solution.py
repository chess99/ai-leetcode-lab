# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
  inf=10**18; d=[[inf]*26 for _ in range(26)]
  for i in range(26):d[i][i]=0
  for a,b,c in zip(original,changed,cost): d[ord(a)-97][ord(b)-97]=min(d[ord(a)-97][ord(b)-97],c)
  for k in range(26):
   for i in range(26):
    for j in range(26):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
  ans=sum(d[ord(a)-97][ord(b)-97] for a,b in zip(source,target))
  return -1 if ans>=inf else ans
