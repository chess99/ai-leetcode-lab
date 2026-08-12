# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:01:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        difference = sum(array1) - sum(array2)
        if difference % 2:
            return []
        half = difference // 2
        values2 = set(array2)
        for value in array1:
            if value - half in values2:
                return [value, value - half]
        return []
