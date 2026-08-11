# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:14:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        pivot = len(arr) - 2
        while pivot >= 0 and arr[pivot] <= arr[pivot + 1]:
            pivot -= 1
        if pivot < 0:
            return arr

        candidate = len(arr) - 1
        while arr[candidate] >= arr[pivot] or (
            candidate > pivot + 1 and arr[candidate] == arr[candidate - 1]
        ):
            candidate -= 1
        arr[pivot], arr[candidate] = arr[candidate], arr[pivot]
        return arr
