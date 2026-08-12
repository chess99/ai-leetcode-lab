# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
 def replaceWords(self,dictionary,sentence):
  roots={}
  for word in dictionary:
   node=roots
   for char in word:node=node.setdefault(char,{})
   node['#']=True
  def f(w):
   node=roots
   for i,char in enumerate(w):
    if '#' in node:return w[:i]
    if char not in node:break
    node=node[char]
   if '#' in node:return w
   return w
  return ' '.join(map(f,sentence.split()))
