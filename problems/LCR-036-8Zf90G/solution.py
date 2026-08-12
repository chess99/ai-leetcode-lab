# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def evalRPN(self,tokens:List[str])->int:
  s=[]
  for x in tokens:
   if x not in '+-*/':s.append(int(x))
   else:
    b=s.pop();a=s.pop();s.append({'+':a+b,'-':a-b,'*':a*b,'/':int(a/b)}[x])
  return s[0]
