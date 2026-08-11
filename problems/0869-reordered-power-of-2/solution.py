# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        signature = sorted(str(n))
        return any(signature == sorted(str(1 << exponent)) for exponent in range(31))
