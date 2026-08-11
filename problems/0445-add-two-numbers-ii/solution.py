# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional
class Solution:
 def addTwoNumbers(self,l1:Optional["ListNode"],l2:Optional["ListNode"])->Optional["ListNode"]:
  a=[];b=[]
  while l1:a.append(l1.val);l1=l1.next
  while l2:b.append(l2.val);l2=l2.next
  c=0;h=None
  while a or b or c:
   c,d=divmod((a.pop() if a else 0)+(b.pop() if b else 0)+c,10);h=ListNode(d,h)
  return h
