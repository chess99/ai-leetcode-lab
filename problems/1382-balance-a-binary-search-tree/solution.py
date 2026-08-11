from __future__ import annotations
class Solution:
 def balanceBST(self,root:TreeNode)->TreeNode:
  a=[]
  def walk(n):
   if n:walk(n.left);a.append(n);walk(n.right)
  def build(l,r):
   if l>=r:return None
   m=(l+r)//2;n=a[m];n.left=build(l,m);n.right=build(m+1,r);return n
  walk(root);return build(0,len(a))
