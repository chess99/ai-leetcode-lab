# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:15:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        index = 0
        while index + 1 < len(arr) and arr[index] < arr[index + 1]:
            index += 1
        if index == 0 or index == len(arr) - 1:
            return False
        while index + 1 < len(arr) and arr[index] > arr[index + 1]:
            index += 1
        return index == len(arr) - 1
