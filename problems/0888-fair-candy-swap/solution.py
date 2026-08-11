# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:08:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob = set(bobSizes)
        for value in aliceSizes:
            if value - diff in bob:
                return [value, value - diff]
