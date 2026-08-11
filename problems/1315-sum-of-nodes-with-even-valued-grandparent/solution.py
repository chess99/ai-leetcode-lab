from __future__ import annotations
class Solution:
 def sumEvenGrandparent(self,root:TreeNode)->int:
  ans=0;stack=[(root,None,None)]
  while stack:
   n,p,g=stack.pop()
   if not n:continue
   if g is not None and g.val%2==0:ans+=n.val
   stack.extend([(n.left,n,p),(n.right,n,p)])
  return ans
