# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod = 1_000_000_007
        velnarqido = (n, pos, k)
        if k > n - 1:
            return 0
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod
        return 2 * fact[n - 1] * pow(fact[k] * fact[n - 1 - k] % mod, mod - 2, mod) % mod
