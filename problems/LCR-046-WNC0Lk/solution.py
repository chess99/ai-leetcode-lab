# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:32Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
class Solution:
 def rightSideView(self,root):
  if not root:return []
  q=deque([root]);r=[]
  while q:
   r.append(q[-1].val)
   for _ in range(len(q)):
    x=q.popleft();q.extend(y for y in (x.left,x.right) if y)
  return r
