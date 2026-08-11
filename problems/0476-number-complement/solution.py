# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:40:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findComplement(self, num: int) -> int:
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
