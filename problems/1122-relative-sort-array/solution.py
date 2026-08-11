# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:35:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        counts = Counter(arr1)
        result = []
        for value in arr2:
            result.extend([value] * counts.pop(value))
        for value in sorted(counts):
            result.extend([value] * counts[value])
        return result
