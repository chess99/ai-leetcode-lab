# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        modulo = 10**9 + 7
        ways = [0] * (high + 1)
        ways[0] = 1
        answer = 0

        for length in range(1, high + 1):
            if length >= zero:
                ways[length] += ways[length - zero]
            if length >= one:
                ways[length] += ways[length - one]
            ways[length] %= modulo

            if length >= low:
                answer = (answer + ways[length]) % modulo

        return answer
