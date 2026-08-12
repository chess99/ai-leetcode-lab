# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for char in expression:
            if char == ',':
                continue
            if char != ')':
                stack.append(char)
                continue
            values = []
            while stack[-1] != '(':
                values.append(stack.pop() == 't')
            stack.pop()
            operation = stack.pop()
            if operation == '!':
                result = not values[0]
            elif operation == '&':
                result = all(values)
            else:
                result = any(values)
            stack.append('t' if result else 'f')
        return stack[-1] == 't'
