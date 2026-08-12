# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:33Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
class Solution:
 def pathSum(self,root,targetSum):
  d=defaultdict(int);d[0]=1
  def f(x,s):
   if not x:return 0
   s+=x.val;r=d[s-targetSum];d[s]+=1;r+=f(x.left,s)+f(x.right,s);d[s]-=1;return r
  return f(root,0)
