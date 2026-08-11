# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:04:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def concatHex36(self, n: int) -> str:
        def to_base(value: int, base: int) -> str:
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = []
            while value:
                result.append(digits[value % base])
                value //= base
            return "".join(reversed(result))

        return to_base(n * n, 16) + to_base(n * n * n, 36)
