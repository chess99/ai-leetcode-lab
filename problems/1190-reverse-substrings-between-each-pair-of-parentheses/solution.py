# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:26:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[[]]
        for ch in s:
            if ch=='(': stack.append([])
            elif ch==')': stack[-2].extend(reversed(stack.pop()))
            else: stack[-1].append(ch)
        return ''.join(stack[0])
