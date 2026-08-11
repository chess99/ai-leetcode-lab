# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def maximumEnergy(self, energy: List[int], k: int) -> int:
  for i in range(len(energy)-k-1,-1,-1):energy[i]+=energy[i+k]
  return max(energy)
