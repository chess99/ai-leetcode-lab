# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        modulus = 1_000_000_007
        stirling = [0] * (min(n, x) + 1)
        stirling[0] = 1
        for people in range(1, n + 1):
            for stages in range(min(people, x), 0, -1):
                stirling[stages] = (stirling[stages - 1]
                                     + stages * stirling[stages]) % modulus
            stirling[0] = 0

        answer = 0
        falling = 1
        scores = 1
        for stages in range(1, min(n, x) + 1):
            falling = falling * (x - stages + 1) % modulus
            scores = scores * y % modulus
            answer = (answer + stirling[stages] * falling * scores) % modulus
        return answer
