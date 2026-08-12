# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        ravolqedin = (n, k)
        mod = 1_000_000_007
        factorial = [1] * (n + 1)
        for value in range(1, n + 1):
            factorial[value] = factorial[value - 1] * value % mod

        # 全部奇数的正整数序列：令每项为 2x+1，和为 n 时 x 和为 (n-k)/2。
        def choose(top, bottom):
            if bottom < 0 or bottom > top:
                return 0
            denominator = factorial[bottom] * factorial[top - bottom] % mod
            return factorial[top] * pow(denominator, mod - 2, mod) % mod
        return (choose(n - 1, k - 1) - (choose((n - k) // 2 + k - 1, k - 1) if (n - k) % 2 == 0 else 0)) % mod
