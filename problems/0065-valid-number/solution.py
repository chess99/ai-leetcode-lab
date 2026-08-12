# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_dot = seen_exponent = False
        digit_after_exponent = True
        for index, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                digit_after_exponent = True
            elif char in "+-":
                if index and s[index - 1] not in "eE":
                    return False
                digit_after_exponent = False
            elif char == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif char in "eE":
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                digit_after_exponent = False
            else:
                return False
        return seen_digit and digit_after_exponent
