# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:35Z
# Experiment: ai-leetcode-lab, round 1
from functools import cache


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @cache
        def solve(value: int) -> int:
            if value <= y:
                return y - value
            answer = value - y
            for divisor in (5, 11):
                quotient, remainder = divmod(value, divisor)
                answer = min(answer, remainder + 1 + solve(quotient))
                if remainder:
                    answer = min(answer, divisor - remainder + 1 + solve(quotient + 1))
            return answer

        return solve(x)
