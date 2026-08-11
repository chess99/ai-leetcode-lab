# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:10:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] != char and stack[-1].lower() == char.lower():
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
