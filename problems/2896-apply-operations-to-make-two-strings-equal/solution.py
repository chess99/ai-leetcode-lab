# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        positions = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]
        if len(positions) % 2:
            return -1
        previous, current = 0, x
        for index in range(1, len(positions)):
            previous, current = current, min(previous + 2 * (positions[index] - positions[index - 1]), current + x)
        return current // 2 if positions else 0
