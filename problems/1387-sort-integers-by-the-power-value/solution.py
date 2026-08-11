from functools import lru_cache
class Solution:
 def getKth(self,lo:int,hi:int,k:int)->int:
  @lru_cache(None)
  def p(x):return 0 if x==1 else 1+p(x//2 if x%2==0 else 3*x+1)
  return sorted(range(lo,hi+1),key=lambda x:(p(x),x))[k-1]
