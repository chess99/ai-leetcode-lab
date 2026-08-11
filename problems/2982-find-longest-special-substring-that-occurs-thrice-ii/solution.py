# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def maximumLength(self, s: str) -> int:
  runs={c:[] for c in 'abcdefghijklmnopqrstuvwxyz'}; i=0
  while i<len(s):
   j=i
   while j<len(s) and s[j]==s[i]:j+=1
   runs[s[i]].append(j-i); i=j
  ans=0
  for a in runs.values():
   a=sorted(a,reverse=True)+[0,0,0]
   ans=max(ans,a[0]-2,min(a[0]-1,a[1]),a[2])
  return ans if ans>0 else -1
