# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 1 << 32
        digits = "0123456789abcdef"
        result = []
        while num:
            result.append(digits[num & 15])
            num >>= 4
        return "".join(reversed(result))
