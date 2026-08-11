# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:29:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_position = {digit: index for index, digit in enumerate(digits)}
        for index, digit in enumerate(digits):
            for larger in map(str, range(9, int(digit), -1)):
                if last_position.get(larger, -1) > index:
                    other = last_position[larger]
                    digits[index], digits[other] = digits[other], digits[index]
                    return int("".join(digits))
        return num
