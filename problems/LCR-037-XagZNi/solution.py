# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def asteroidCollision(self,asteroids:List[int])->List[int]:
  s=[]
  for a in asteroids:
   while s and a<0<s[-1] and s[-1]<-a:s.pop()
   if s and a<0<s[-1]:
    if s[-1]==-a:s.pop()
   else:s.append(a)
  return s
