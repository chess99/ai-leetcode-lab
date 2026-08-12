# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:35Z
# Experiment: ai-leetcode-lab, round 1
class MyCalendar:
 def __init__(self):self.a=[]
 def book(self,start,end):
  for l,r in self.a:
   if start<r and l<end:return False
  self.a.append((start,end));return True
