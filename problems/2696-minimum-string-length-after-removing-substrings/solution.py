# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:12:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for ch in s:
            if stack and stack[-1] + ch in ('AB', 'CD'):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)
