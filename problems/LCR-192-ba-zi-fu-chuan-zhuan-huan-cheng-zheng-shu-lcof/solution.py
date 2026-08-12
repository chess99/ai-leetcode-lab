# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def myAtoi(self, str: str) -> int:
        index, length = 0, len(str)
        while index < length and str[index] == ' ':
            index += 1
        sign = 1
        if index < length and str[index] in '+-':
            sign = -1 if str[index] == '-' else 1
            index += 1
        value = 0
        limit = 2 ** 31 if sign < 0 else 2 ** 31 - 1
        while index < length and '0' <= str[index] <= '9':
            digit = ord(str[index]) - ord('0')
            if value > (limit - digit) // 10:
                return -2 ** 31 if sign < 0 else 2 ** 31 - 1
            value = value * 10 + digit
            index += 1
        return sign * value
