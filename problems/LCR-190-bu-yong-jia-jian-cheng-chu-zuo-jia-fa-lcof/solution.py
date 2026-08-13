# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:52:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        mask = 0xFFFFFFFF
        max_signed = 0x7FFFFFFF
        dataA &= mask
        dataB &= mask
        while dataB:
            dataA, dataB = (dataA ^ dataB) & mask, ((dataA & dataB) << 1) & mask
        return dataA if dataA <= max_signed else ~(dataA ^ mask)
