# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:08:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            stack.append(char)
            if len(stack)>=3 and stack[-3:]==['a','b','c']: del stack[-3:]
        return not stack
