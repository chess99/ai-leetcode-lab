# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:39Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
 def minAnagramLength(self, s: str) -> int:
  for k in range(1,len(s)+1):
   if len(s)%k==0 and all(Counter(s[i:i+k])==Counter(s[:k]) for i in range(k,len(s),k)):return k
