# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for index in range(1, len(nums), 2):
            nums[index - 1], nums[index] = nums[index], nums[index - 1]
