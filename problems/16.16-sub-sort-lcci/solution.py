# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:01:02Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        right = -1
        maximum = float("-inf")
        for index, value in enumerate(array):
            if value < maximum:
                right = index
            maximum = max(maximum, value)
        if right == -1:
            return [-1, -1]
        left = 0
        minimum = float("inf")
        for index in range(len(array) - 1, -1, -1):
            if array[index] > minimum:
                left = index
            minimum = min(minimum, array[index])
        return [left, right]
