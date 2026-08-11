# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:44:37Z
# Experiment: ai-leetcode-lab, round 1
from functools import cache
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def compute(text: str):
            results = []
            for index, char in enumerate(text):
                if char in "+-*":
                    for left in compute(text[:index]):
                        for right in compute(text[index + 1:]):
                            if char == "+":
                                results.append(left + right)
                            elif char == "-":
                                results.append(left - right)
                            else:
                                results.append(left * right)
            return results or [int(text)]

        return compute(expression)
