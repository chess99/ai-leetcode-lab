# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        modulus = 1_000_000_007
        a = e = i = o = u = 1
        for _ in range(1, n):
            a, e, i, o, u = ((e + i + u) % modulus,
                             (a + i) % modulus,
                             (e + o) % modulus,
                             i,
                             (i + o) % modulus)
        return (a + e + i + o + u) % modulus
