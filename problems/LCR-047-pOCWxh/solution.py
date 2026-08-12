# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def pruneTree(self,root):
  if not root:return None
  root.left=self.pruneTree(root.left);root.right=self.pruneTree(root.right)
  return root if root.val or root.left or root.right else None
