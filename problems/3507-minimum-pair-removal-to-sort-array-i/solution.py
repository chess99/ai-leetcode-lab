# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:03:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        while any(nums[i] > nums[i + 1] for i in range(len(nums) - 1)):
            index = min(range(len(nums) - 1), key=lambda i: nums[i] + nums[i + 1])
            nums[index : index + 2] = [nums[index] + nums[index + 1]]
            operations += 1
        return operations
