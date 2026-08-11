# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def minEnd(self, n: int, x: int) -> int:
  n-=1; bit=0
  while n:
   if not (x>>bit)&1:
    x|=(n&1)<<bit; n>>=1
   bit+=1
  return x
