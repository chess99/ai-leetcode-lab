# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:30:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        for i, value in enumerate(nums):
            if value != 0:
                nums[write], nums[i] = nums[i], nums[write]
                write += 1
