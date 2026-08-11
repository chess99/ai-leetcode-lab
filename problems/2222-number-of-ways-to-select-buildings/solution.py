# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def numberOfWays(self,s:str)->int:
  z=s.count('0');o=len(s)-z; lz=lo=ans=0
  for c in s:
   if c=='0': ans+=lo*(o-lo); lz+=1
   else: ans+=lz*(z-lz); lo+=1
  return ans
