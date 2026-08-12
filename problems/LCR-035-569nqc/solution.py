# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def findMinDifference(self,timePoints:List[str])->int:
  a=sorted(int(x[:2])*60+int(x[3:]) for x in timePoints)
  if len(a)!=len(set(a)):return 0
  return min([b-a for a,b in zip(a,a[1:])]+[a[0]+1440-a[-1]])
