# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:29Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        digits = list(str(abs(num)))

        if num < 0:
            digits.sort(reverse=True)
            return -int("".join(digits))

        digits.sort()
        first_nonzero = next(
            index for index, digit in enumerate(digits) if digit != "0"
        )
        digits[0], digits[first_nonzero] = digits[first_nonzero], digits[0]
        return int("".join(digits))
