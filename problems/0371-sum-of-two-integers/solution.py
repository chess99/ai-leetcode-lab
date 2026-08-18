# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = ~((~0) << 32)
        sign_bit = 1 << 31

        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a < sign_bit else ~(a ^ mask)
