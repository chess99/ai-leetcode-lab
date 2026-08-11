# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
 def validSubstringCount(self, word1: str, word2: str) -> int:
  need=Counter(word2);have=Counter();left=ans=0
  for right,c in enumerate(word1):
   have[c]+=1
   while all(have[x]>=v for x,v in need.items()):
    ans+=len(word1)-right;have[word1[left]]-=1;left+=1
  return ans
