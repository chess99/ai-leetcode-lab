# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:52:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        while dataB:
            dataA, dataB = dataA ^ dataB, (dataA & dataB) << 1
        return dataA
