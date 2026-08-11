# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:30:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removed = set()
        for index, character in enumerate(s):
            if character == '(':
                stack.append(index)
            elif character == ')':
                if stack:
                    stack.pop()
                else:
                    removed.add(index)
        removed.update(stack)
        return ''.join(character for index, character in enumerate(s) if index not in removed)
