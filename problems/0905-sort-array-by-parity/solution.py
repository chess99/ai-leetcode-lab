# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:11:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] % 2 == 0: left += 1
            if nums[right] % 2 == 1: right -= 1
        return nums
