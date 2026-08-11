# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:52:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]; current=''; number=0
        for c in s:
            if c.isdigit():number=number*10+int(c)
            elif c=='[':stack.append((current,number));current='';number=0
            elif c==']':prefix,count=stack.pop();current=prefix+current*count
            else:current+=c
        return current
