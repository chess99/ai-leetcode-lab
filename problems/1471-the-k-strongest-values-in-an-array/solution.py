# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:52:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        left, right = 0, len(arr) - 1
        result = []
        while len(result) < k:
            if abs(arr[right] - median) >= abs(arr[left] - median):
                result.append(arr[right]); right -= 1
            else:
                result.append(arr[left]); left += 1
        return result
