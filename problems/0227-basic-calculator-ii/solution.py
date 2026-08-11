# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:33:55Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def calculate(self, s: str) -> int:
        stack, number, operator = [], 0, "+"
        for char in s + "+":
            if char.isdigit():
                number = number * 10 + int(char)
            elif char != " ":
                if operator == "+": stack.append(number)
                elif operator == "-": stack.append(-number)
                elif operator == "*": stack[-1] *= number
                else: stack[-1] = int(stack[-1] / number)
                operator, number = char, 0
        return sum(stack)
