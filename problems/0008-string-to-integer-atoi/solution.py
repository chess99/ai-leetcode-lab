# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:07:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        length = len(s)
        while index < length and s[index] == " ":
            index += 1

        sign = 1
        if index < length and s[index] in "+-":
            sign = -1 if s[index] == "-" else 1
            index += 1

        value = 0
        limit = 2**31 if sign == -1 else 2**31 - 1
        while index < length and s[index].isdigit():
            digit = ord(s[index]) - ord("0")
            if value > (limit - digit) // 10:
                return -2**31 if sign == -1 else 2**31 - 1
            value = value * 10 + digit
            index += 1
        return sign * value
