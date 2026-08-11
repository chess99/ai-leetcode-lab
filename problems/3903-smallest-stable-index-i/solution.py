# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:20:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        suffix_min = [0] * len(nums)
        suffix_min[-1] = nums[-1]
        for index in range(len(nums) - 2, -1, -1):
            suffix_min[index] = min(nums[index], suffix_min[index + 1])

        prefix_max = nums[0]
        for index, num in enumerate(nums):
            prefix_max = max(prefix_max, num)
            if prefix_max - suffix_min[index] <= k:
                return index
        return -1
