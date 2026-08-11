# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:59:29Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        value = n ^ (n >> 1)
        return value & (value + 1) == 0
