# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        suffix_min = nums[-1]
        minima = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            suffix_min = min(suffix_min, nums[i])
            minima[i] = suffix_min
        prefix = 0
        answer = -10**30
        for i in range(len(nums) - 1):
            prefix += nums[i]
            answer = max(answer, prefix - minima[i + 1])
        return answer
