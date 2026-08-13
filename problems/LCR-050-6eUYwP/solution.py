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
  if not root:return 0
  answer=0;stack=[(root,0,False)]
  while stack:
   node,prefix,leaving=stack.pop()
   if leaving:
    d[prefix]-=1
    continue
   prefix+=node.val;answer+=d[prefix-targetSum];d[prefix]+=1
   stack.append((node,prefix,True))
   if node.right:stack.append((node.right,prefix,False))
   if node.left:stack.append((node.left,prefix,False))
  return answer
