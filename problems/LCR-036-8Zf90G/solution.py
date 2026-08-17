# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                value = left + right
            elif token == "-":
                value = left - right
            elif token == "*":
                value = left * right
            else:
                # 只用整数运算实现向零截断，避免大整数转 float 溢出或丢失精度。
                quotient = abs(left) // abs(right)
                value = -quotient if (left < 0) != (right < 0) else quotient

            stack.append(value)

        return stack[0]
