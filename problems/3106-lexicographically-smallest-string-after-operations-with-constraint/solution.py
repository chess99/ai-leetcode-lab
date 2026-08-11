# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def getSmallestString(self, s: str, k: int) -> str:
  out=[]
  for ch in s:
   x=ord(ch)-97; cost=min(x,26-x)
   if cost<=k: out.append('a'); k-=cost
   else: out.append(chr(97+x-k)); k=0
  return ''.join(out)
