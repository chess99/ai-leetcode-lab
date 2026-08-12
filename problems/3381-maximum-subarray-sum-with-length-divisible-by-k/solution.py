# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        minimum = [float('inf')] * k
        minimum[0] = 0
        prefix = 0
        answer = -float('inf')
        for i, value in enumerate(nums, 1):
            prefix += value
            rem = i % k
            answer = max(answer, prefix - minimum[rem])
            minimum[rem] = min(minimum[rem], prefix)
        return answer
