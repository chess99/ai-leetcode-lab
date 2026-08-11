# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def compress(self,chars:List[str])->int:
  r=w=0
  while r<len(chars):
   s=r
   while r<len(chars) and chars[r]==chars[s]:r+=1
   chars[w]=chars[s];w+=1
   if r-s>1:
    for d in str(r-s):chars[w]=d;w+=1
  return w
