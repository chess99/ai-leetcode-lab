# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def findAnagrams(self,s:str,p:str)->List[int]:
  if len(p)>len(s): return []
  a=[0]*26;b=[0]*26
  for c in p:a[ord(c)-97]+=1
  r=[]
  for i,c in enumerate(s):
   b[ord(c)-97]+=1
   if i>=len(p):b[ord(s[i-len(p)])-97]-=1
   if a==b:r.append(i-len(p)+1)
  return r
