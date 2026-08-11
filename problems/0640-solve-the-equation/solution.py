# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:27:16Z
# Experiment: ai-leetcode-lab, round 1
import re


class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(side: str) -> tuple[int, int]:
            coefficient = 0
            constant = 0
            for term in re.findall(r"[+-]?\d*x|[+-]?\d+", side):
                if term.endswith("x"):
                    value = term[:-1]
                    coefficient += 1 if value in ("", "+") else -1 if value == "-" else int(value)
                else:
                    constant += int(term)
            return coefficient, constant

        left_coefficient, left_constant = parse(equation.split("=")[0])
        right_coefficient, right_constant = parse(equation.split("=")[1])
        coefficient = left_coefficient - right_coefficient
        constant = right_constant - left_constant
        if coefficient == 0:
            return "Infinite solutions" if constant == 0 else "No solution"
        return f"x={constant // coefficient}"
