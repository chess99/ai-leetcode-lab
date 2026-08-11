# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:24:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def finalString(self, s: str) -> str:
        from collections import deque

        chars = deque()
        reversed_order = False
        for char in s:
            if char == "i":
                reversed_order = not reversed_order
            elif reversed_order:
                chars.appendleft(char)
            else:
                chars.append(char)

        return "".join(reversed(chars) if reversed_order else chars)
