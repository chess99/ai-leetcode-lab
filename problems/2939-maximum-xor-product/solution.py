# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod = 10 ** 9 + 7
        left, right = (a >> n) << n, (b >> n) << n
        for bit in range(n - 1, -1, -1):
            mask = 1 << bit
            if bool(a & mask) == bool(b & mask):
                left |= mask
                right |= mask
            elif left < right:
                left |= mask
            else:
                right |= mask
        return (left * right) % mod
