# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:16:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        mask = (1 << n.bit_length()) - 1
        return n ^ mask
