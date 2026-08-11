# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:37:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for index in range(1, len(nums)):
            needed = nums[index - 1] + 1
            if nums[index] < needed:
                operations += needed - nums[index]
                nums[index] = needed
        return operations
