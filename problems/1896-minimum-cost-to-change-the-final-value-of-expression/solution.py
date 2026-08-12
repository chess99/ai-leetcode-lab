# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:51:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        values = []
        operators = []

        def combine():
            right = values.pop()
            left = values.pop()
            operator = operators.pop()
            result = [10 ** 9, 10 ** 9]
            for left_value in (0, 1):
                for right_value in (0, 1):
                    base_cost = left[left_value] + right[right_value]
                    for chosen_operator in "&|":
                        if chosen_operator == "&":
                            target = left_value & right_value
                        else:
                            target = left_value | right_value
                        result[target] = min(
                            result[target],
                            base_cost + (chosen_operator != operator),
                        )
            values.append(result)

        for char in expression:
            if char in "01":
                values.append([0 if char == "0" else 1,
                               0 if char == "1" else 1])
            elif char in "&|":
                while operators and operators[-1] != "(":
                    combine()
                operators.append(char)
            elif char == "(":
                operators.append(char)
            else:
                while operators[-1] != "(":
                    combine()
                operators.pop()

        while operators:
            combine()
        return values[0][1 if values[0][0]==0 else 0]
