# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:18Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
 def findWinners(self,matches:List[List[int]])->List[List[int]]:
  losses=defaultdict(int)
  for w,l in matches: losses[w]+=0; losses[l]+=1
  return [sorted(x for x in losses if losses[x]==0),sorted(x for x in losses if losses[x]==1)]
