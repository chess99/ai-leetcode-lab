# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:05:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up = down = best = 1
        for index in range(1, len(arr)):
            if arr[index] > arr[index-1]: up, down = down + 1, 1
            elif arr[index] < arr[index-1]: up, down = 1, up + 1
            else: up = down = 1
            best = max(best, up, down)
        return best
