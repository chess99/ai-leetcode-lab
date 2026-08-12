# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def inorderSuccessor(self,root,p):
  ans=None
  while root:
   if root.val>p.val:ans=root;root=root.left
   else:root=root.right
  return ans
