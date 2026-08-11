from collections import Counter,deque
from typing import List
class Solution:
 def watchedVideosByFriends(self,w:List[List[str]],f:List[List[int]],id:int,level:int)->List[str]:
  q=deque([id]);seen={id}
  for _ in range(level):
   for _ in range(len(q)):
    for v in f[q.popleft()]:
     if v not in seen:seen.add(v);q.append(v)
  return sorted(Counter(x for p in q for x in w[p]).keys(),key=lambda x:(sum(x in w[p] for p in q),x))
