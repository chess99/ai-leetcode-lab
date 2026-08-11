# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxDiff(self, num: int) -> int:
        digits = str(num)
        maximum = digits
        for digit in digits:
            if digit != "9":
                maximum = digits.replace(digit, "9")
                break

        if digits[0] != "1":
            minimum = digits.replace(digits[0], "1")
        else:
            minimum = digits
            for digit in digits[1:]:
                if digit not in "01":
                    minimum = digits.replace(digit, "0")
                    break
        return int(maximum) - int(minimum)
