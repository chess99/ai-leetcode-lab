# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
import heapq
class Solution:
 def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
  g=[[] for _ in range(n)]
  for a,b,w in edges:g[a].append((b,w));g[b].append((a,w))
  d=[-1]*n; d[0]=0; q=[(0,0)]
  while q:
   t,u=heapq.heappop(q)
   if t!=d[u]:continue
   for v,w in g[u]:
    nt=t+w
    if nt<disappear[v] and (d[v]<0 or nt<d[v]):d[v]=nt;heapq.heappush(q,(nt,v))
  return d
