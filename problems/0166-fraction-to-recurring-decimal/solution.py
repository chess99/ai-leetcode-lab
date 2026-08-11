# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:29:21Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        negative = (numerator < 0) != (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        integer, remainder = divmod(numerator, denominator)
        result = ["-" if negative else "", str(integer)]
        if remainder == 0:
            return "".join(result)
        result.append(".")
        seen = {}
        while remainder:
            if remainder in seen:
                result.insert(seen[remainder], "(")
                result.append(")")
                break
            seen[remainder] = len(result)
            remainder *= 10
            digit, remainder = divmod(remainder, denominator)
            result.append(str(digit))
        return "".join(result)
