# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for char in s:
            if char.isdigit():stack.pop()
            else:stack.append(char)
        return ''.join(stack)
