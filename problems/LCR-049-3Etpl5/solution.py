# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def sumNumbers(self,root):
  def f(x,v):return 0 if not x else v*10+x.val if not x.left and not x.right else f(x.left,v*10+x.val)+f(x.right,v*10+x.val)
  return f(root,0)
