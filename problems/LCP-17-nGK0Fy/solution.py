# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:26:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for operation in s:
            if operation == 'A':
                x = 2 * x + y
            else:
                y = 2 * y + x
        return x + y
