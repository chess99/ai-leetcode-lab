# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        limit = sum(nums) + 1
        suffix = [1] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = min(limit, suffix[i + 1] * nums[i])
        left = 0
        for i, value in enumerate(nums):
            if left == suffix[i + 1]:
                return i
            left += value
        return -1
