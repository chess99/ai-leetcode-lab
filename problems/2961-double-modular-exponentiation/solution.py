# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
  return [i for i,(a,b,c,m) in enumerate(variables) if pow(pow(a,b,10),c,m)==target]
