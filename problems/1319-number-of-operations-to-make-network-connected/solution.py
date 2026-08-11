from typing import List
class Solution:
 def makeConnected(self,n:int,connections:List[List[int]])->int:
  if len(connections)<n-1:return -1
  p=list(range(n))
  def f(x):
   while p[x]!=x:p[x]=p[p[x]];x=p[x]
   return x
  for a,b in connections:p[f(a)]=f(b)
  return len({f(i) for i in range(n)})-1
