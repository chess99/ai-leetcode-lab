# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
  h=[1]+hFences+[m]; v=[1]+vFences+[n]
  ds={h[j]-h[i] for i in range(len(h)) for j in range(i+1,len(h))}
  side=max((v[j]-v[i] for i in range(len(v)) for j in range(i+1,len(v)) if v[j]-v[i] in ds),default=0)
  return side*side%(10**9+7) if side else -1
