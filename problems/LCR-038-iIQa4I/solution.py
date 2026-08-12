# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def dailyTemperatures(self,temperatures:List[int])->List[int]:
  r=[0]*len(temperatures);s=[]
  for i,x in enumerate(temperatures):
   while s and temperatures[s[-1]]<x:j=s.pop();r[j]=i-j
   s.append(i)
  return r
