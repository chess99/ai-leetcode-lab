# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def convertBST(self,root):
  total=0;stack=[];node=root
  while stack or node:
   while node:stack.append(node);node=node.right
   node=stack.pop();total+=node.val;node.val=total;node=node.left
  return root
