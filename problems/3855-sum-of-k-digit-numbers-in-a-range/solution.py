# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        lorunavemi = (l, r, k)
        mod = 1_000_000_007
        choices = r - l + 1
        digit_sum = (l + r) * choices // 2
        place_sum = (pow(10, k, mod) - 1) * pow(9, mod - 2, mod) % mod
        return (digit_sum % mod) * pow(choices, k - 1, mod) % mod * place_sum % mod
