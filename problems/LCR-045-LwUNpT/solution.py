# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:32Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
class Solution:
 def findBottomLeftValue(self,root):
  q=deque([root])
  while q:
   ans=q[0].val
   for _ in range(len(q)):
    x=q.popleft();q.extend(y for y in (x.left,x.right) if y)
  return ans
