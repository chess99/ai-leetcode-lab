# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        size = len(nums)
        score = [[0] * size for _ in range(size)]
        best = [[0] * size for _ in range(size)]
        for index, value in enumerate(nums):
            score[index][index] = best[index][index] = value
        for length in range(2, size + 1):
            for left in range(size - length + 1):
                right = left + length - 1
                score[left][right] = score[left][right - 1] ^ score[left + 1][right]
                best[left][right] = max(score[left][right],
                                        best[left + 1][right],
                                        best[left][right - 1])
        return [best[left][right] for left, right in queries]
