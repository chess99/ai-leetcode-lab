# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def calculate(self, s: str) -> int:
        total = term = number = 0
        operator = '+'
        for char in s + '+':
            if char.isdigit():
                number = number * 10 + ord(char) - ord('0')
            elif char != ' ':
                if operator == '+':
                    total += term
                    term = number
                elif operator == '-':
                    total += term
                    term = -number
                elif operator == '*':
                    term *= number
                else:
                    quotient = abs(term) // number
                    term = quotient if term >= 0 else -quotient
                operator, number = char, 0
        return total + term
