# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:44:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numTilings(self, n: int) -> int:
        modulo = 1_000_000_007
        if n <= 2:
            return n
        first, second, third = 1, 2, 5
        for _ in range(4, n + 1):
            first, second, third = second, third, (2 * third + first) % modulo
        return third
