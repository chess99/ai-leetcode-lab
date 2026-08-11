# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:37:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {value: index for index, value in enumerate(arr2)}
        return sorted(arr1, key=lambda value: (order.get(value, len(arr2)), value))
