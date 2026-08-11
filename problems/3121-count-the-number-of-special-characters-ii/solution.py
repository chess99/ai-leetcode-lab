# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def numberOfSpecialChars(self, word: str) -> int:
  first=[len(word)]*26; last=[-1]*26
  for i,ch in enumerate(word):
   x=ord(ch.lower())-97
   if ch.isupper():first[x]=min(first[x],i)
   else:last[x]=i
  return sum(last[i]>=0 and first[i]<len(word) and last[i]<first[i] for i in range(26))
