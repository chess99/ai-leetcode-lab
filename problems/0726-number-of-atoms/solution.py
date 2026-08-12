# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        from collections import Counter

        stack = [Counter()]
        index = 0
        while index < len(formula):
            char = formula[index]
            if char == '(':
                stack.append(Counter())
                index += 1
            elif char == ')':
                index += 1
                start = index
                while index < len(formula) and formula[index].isdigit():
                    index += 1
                multiplier = int(formula[start:index] or '1')
                group = stack.pop()
                for atom, count in group.items():
                    stack[-1][atom] += count * multiplier
            else:
                start = index
                index += 1
                while index < len(formula) and formula[index].islower():
                    index += 1
                atom = formula[start:index]
                start = index
                while index < len(formula) and formula[index].isdigit():
                    index += 1
                stack[-1][atom] += int(formula[start:index] or '1')
        return ''.join(atom + (str(count) if count > 1 else '')
                       for atom, count in sorted(stack[0].items()))
