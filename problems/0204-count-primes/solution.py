# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:31:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        prime = bytearray(b"\x01") * n
        prime[0:2] = b"\x00\x00"
        for value in range(2, int(n**0.5) + 1):
            if prime[value]:
                prime[value * value:n:value] = b"\x00" * len(prime[value * value:n:value])
        return sum(prime)
