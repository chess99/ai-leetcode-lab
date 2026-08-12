# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:35Z
# Experiment: ai-leetcode-lab, round 1
class BSTIterator:
 def __init__(self,root):self.s=[];self._push(root)
 def _push(self,x):
  while x:self.s.append(x);x=x.left
 def next(self):
  x=self.s.pop();self._push(x.right);return x.val
 def hasNext(self):return bool(self.s)
