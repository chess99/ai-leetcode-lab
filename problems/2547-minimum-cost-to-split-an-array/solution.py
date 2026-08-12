# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        size = len(nums)
        dynamic = [0] + [10 ** 30] * size
        for end in range(1, size + 1):
            frequencies = [0] * size
            trimmed = 0
            for start in range(end - 1, -1, -1):
                value = nums[start]
                frequencies[value] += 1
                if frequencies[value] == 2:
                    trimmed += 2
                elif frequencies[value] > 2:
                    trimmed += 1
                dynamic[end] = min(dynamic[end], dynamic[start] + k + trimmed)
        return dynamic[size]
