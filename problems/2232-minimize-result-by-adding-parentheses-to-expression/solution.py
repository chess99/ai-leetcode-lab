# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def minimizeResult(self,expression:str)->str:
  a,b=expression.split('+'); best=float('inf');ans=''
  for i in range(len(a)):
   for j in range(1,len(b)+1):
    v=int(a[:i] or '1')*(int(a[i:])+int(b[:j]))*int(b[j:] or '1')
    if v<best: best,ans=v,a[:i]+'('+a[i:]+'+'+b[:j]+')'+b[j:]
  return ans
