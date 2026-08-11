# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
from functools import cache
class Solution:
 def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
  mod=10**9+7
  @cache
  def f(z,o,last,run):
   if z==zero and o==one:return 1
   ans=0
   if z<zero and (last!=0 or run<limit):ans+=f(z+1,o,0,run+1 if last==0 else 1)
   if o<one and (last!=1 or run<limit):ans+=f(z,o+1,1,run+1 if last==1 else 1)
   return ans%mod
  return f(0,0,2,0)
