# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:39Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
 def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
  c=Counter(word[i:i+k] for i in range(0,len(word),k))
  return len(word)//k-max(c.values())
