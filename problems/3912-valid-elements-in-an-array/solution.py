# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:20:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        right_max = [-1] * len(nums)
        maximum = -1
        for index in range(len(nums) - 1, -1, -1):
            right_max[index] = maximum
            maximum = max(maximum, nums[index])

        result = []
        left_max = -1
        for index, num in enumerate(nums):
            if num > left_max or num > right_max[index]:
                result.append(num)
            left_max = max(left_max, num)
        return result
