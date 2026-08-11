# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and (abs(ord(stack[-1]) - ord(ch)) == 1 or {stack[-1], ch} == {'a', 'z'}):
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
