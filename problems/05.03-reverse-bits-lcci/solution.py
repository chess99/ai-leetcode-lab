# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:57:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reverseBits(self, num: int) -> int:
        num &= 0xFFFFFFFF
        previous = current = 0
        best = 1
        for _ in range(32):
            if num & 1:
                current += 1
            else:
                previous = current if num & 2 else 0
                current = 0
            best = max(best, previous + 1 + current)
            num >>= 1
        return min(best, 32)
