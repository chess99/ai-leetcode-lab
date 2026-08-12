# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:31Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
class CBTInserter:
 def __init__(self,root):
  self.root=root;self.q=deque();z=deque([root])
  while z:
   x=z.popleft()
   if not x.left or not x.right:self.q.append(x)
   if x.left:z.append(x.left)
   if x.right:z.append(x.right)
 def insert(self,v):
  parent=self.q[0];node=TreeNode(v)
  if not parent.left:parent.left=node
  else:parent.right=node;self.q.popleft()
  self.q.append(node);return parent.val
 def get_root(self):return self.root
