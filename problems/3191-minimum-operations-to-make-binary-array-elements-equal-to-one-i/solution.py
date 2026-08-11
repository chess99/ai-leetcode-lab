# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        for index in range(len(nums) - 2):
            if nums[index] == 0:
                answer += 1
                nums[index] ^= 1
                nums[index + 1] ^= 1
                nums[index + 2] ^= 1
        return answer if all(nums) else -1
