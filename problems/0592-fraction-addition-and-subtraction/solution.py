# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:24:41Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator = 0
        denominator = 1
        for fraction in re.findall(r"[+-]?\d+/\d+", expression):
            current_numerator, current_denominator = map(int, fraction.split("/"))
            numerator = numerator * current_denominator + current_numerator * denominator
            denominator *= current_denominator
            divisor = gcd(abs(numerator), denominator)
            numerator //= divisor
            denominator //= divisor
        return f"{numerator}/{denominator}"
