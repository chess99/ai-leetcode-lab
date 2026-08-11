# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:59:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for start in range(0, len(nums), 3):
            remaining = nums[start:]
            if len(remaining) == len(set(remaining)):
                return operations
            operations += 1
        return operations
