# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
  pos=[i for i,v in enumerate(nums) if v==x]
  return [pos[q-1] if q<=len(pos) else -1 for q in queries]
