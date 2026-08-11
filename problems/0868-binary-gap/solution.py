# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:05:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def binaryGap(self, n: int) -> int:
        previous = None
        best = 0
        position = 0
        while n:
            if n & 1:
                if previous is not None:
                    best = max(best, position - previous)
                previous = position
            n >>= 1
            position += 1
        return best
