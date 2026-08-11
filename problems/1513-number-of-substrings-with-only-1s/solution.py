# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:54:21Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numSub(self, s: str) -> int:
        total = run = 0
        for char in s:
            run = run + 1 if char == '1' else 0
            total += run
        return total % (10 ** 9 + 7)
