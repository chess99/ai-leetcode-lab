# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        best = nums[:]
        answer = sum(best)
        for rotations in range(1, len(nums)):
            for index in range(len(nums)):
                best[index] = min(best[index], nums[(index - rotations) % len(nums)])
            answer = min(answer, sum(best) + rotations * x)
        return answer
