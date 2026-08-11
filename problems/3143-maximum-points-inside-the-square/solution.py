# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
  a=sorted((max(abs(x),abs(y)),c) for (x,y),c in zip(points,s)); seen=set(); ans=i=0
  while i<len(a):
   j=i; cur=set()
   while j<len(a) and a[j][0]==a[i][0]:
    if a[j][1] in seen or a[j][1] in cur:return ans
    cur.add(a[j][1]);j+=1
   seen|=cur;ans+=j-i;i=j
  return ans
