# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:21:21Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zeros = nums.count(0)
        return sum(value != 0 for value in nums[len(nums)-zeros:])
