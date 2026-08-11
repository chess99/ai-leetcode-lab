from collections import defaultdict,deque
from typing import List
class Solution:
 def numOfMinutes(self,n:int,headID:int,manager:List[int],informTime:List[int])->int:
  g=defaultdict(list)
  for i,m in enumerate(manager):g[m].append(i)
  q=deque([(headID,0)]);ans=0
  while q:
   u,t=q.popleft();ans=max(ans,t)
   for v in g[u]:q.append((v,t+informTime[u]))
  return ans
