# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        impossible = -10 ** 9
        maximum_digits = [impossible] * (target + 1)
        maximum_digits[0] = 0
        for value in range(1, target + 1):
            for current_cost in cost:
                if value >= current_cost:
                    maximum_digits[value] = max(
                        maximum_digits[value], maximum_digits[value - current_cost] + 1)
        if maximum_digits[target] < 0:
            return '0'
        answer = []
        remaining = target
        for digit in range(9, 0, -1):
            current_cost = cost[digit - 1]
            while (remaining >= current_cost and
                   maximum_digits[remaining] == maximum_digits[remaining - current_cost] + 1):
                answer.append(str(digit))
                remaining -= current_cost
        return ''.join(answer)
