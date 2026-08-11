# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:12:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        return not stack
