# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def convertBST(self,root):
  s=0
  def f(x):
   nonlocal s
   if x:f(x.right);s+=x.val;x.val=s;f(x.left)
  f(root);return root
