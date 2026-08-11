# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:07:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        index = 1
        while index < len(nums) and nums[index - 1] < nums[index]:
            index += 1
        if index == 1 or index == len(nums):
            return False

        decreasing_start = index
        while index < len(nums) and nums[index - 1] > nums[index]:
            index += 1
        if index == decreasing_start or index == len(nums):
            return False

        while index < len(nums) and nums[index - 1] < nums[index]:
            index += 1
        return index == len(nums)
