# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        starts = [0] * len(nums)
        active = answer = 0
        for index, value in enumerate(nums):
            if index >= k:
                active ^= starts[index - k]
            if value ^ active == 0:
                if index + k > len(nums):
                    return -1
                starts[index] = 1
                active ^= 1
                answer += 1
        return answer
