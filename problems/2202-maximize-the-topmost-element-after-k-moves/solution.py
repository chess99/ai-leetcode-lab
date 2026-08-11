# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        if len(nums) == 1:
            return nums[0] if k % 2 == 0 else -1

        answer = -1

        for index in range(min(len(nums), k - 1)):
            answer = max(answer, nums[index])

        if k < len(nums):
            answer = max(answer, nums[k])

        return answer
