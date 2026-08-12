# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def calculate(self, s: str) -> int:
        total = number = 0; sign = 1; stack = []
        for ch in s + "+":
            if ch.isdigit(): number = number * 10 + int(ch)
            elif ch in "+-": total += sign * number; number = 0; sign = 1 if ch == "+" else -1
            elif ch == "(": stack += [total, sign]; total = 0; sign = 1
            elif ch == ")": total += sign * number; number = 0; total *= stack.pop(); total += stack.pop()
        return total
