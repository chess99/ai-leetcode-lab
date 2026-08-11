# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left, right = 0, max(arr)
        while left < right:
            middle = (left + right) // 2
            if sum(min(value, middle) for value in arr) < target: left = middle + 1
            else: right = middle
        previous = left - 1
        return previous if abs(sum(min(x, previous) for x in arr) - target) <= abs(sum(min(x, left) for x in arr) - target) else left
