# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:57:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        differences = (A ^ B) & 0xFFFFFFFF
        count = 0
        while differences:
            differences &= differences - 1
            count += 1
        return count
