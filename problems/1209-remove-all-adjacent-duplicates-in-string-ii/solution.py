# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:28:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for ch in s:
            if stack and stack[-1][0]==ch: stack[-1][1]+=1
            else: stack.append([ch,1])
            if stack[-1][1]==k: stack.pop()
        return ''.join(ch*count for ch,count in stack)
