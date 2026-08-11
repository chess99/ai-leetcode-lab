# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:05:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(text):
            stack = []
            for char in text:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        return build(s) == build(t)
