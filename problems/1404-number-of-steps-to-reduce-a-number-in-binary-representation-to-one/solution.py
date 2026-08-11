# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:29Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numSteps(self, s: str) -> int:
        steps = carry = 0
        for bit in reversed(s[1:]):
            if int(bit) + carry == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps + carry
