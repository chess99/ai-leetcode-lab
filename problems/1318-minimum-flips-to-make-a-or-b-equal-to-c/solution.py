# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for _ in range(31):
            if c & 1:
                if not (a & 1 or b & 1):
                    flips += 1
            else:
                flips += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
