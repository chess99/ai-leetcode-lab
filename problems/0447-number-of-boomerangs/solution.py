# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:35Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
 def numberOfBoomerangs(self,points:List[List[int]])->int:
  total=0
  for x,y in points:
   d=defaultdict(int)
   for a,b in points:
    k=(x-a)**2+(y-b)**2;total+=2*d[k];d[k]+=1
  return total
