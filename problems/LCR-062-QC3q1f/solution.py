# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:37Z
# Experiment: ai-leetcode-lab, round 1
class Trie:
 def __init__(self):self.d={};self.end=False
 def insert(self,w):
  x=self
  for c in w:x=x.d.setdefault(c,Trie())
  x.end=True
 def search(self,w):
  x=self
  for c in w:
   if c not in x.d:return False
   x=x.d[c]
  return x.end
 def startsWith(self,p):
  x=self
  for c in p:
   if c not in x.d:return False
   x=x.d[c]
  return True
