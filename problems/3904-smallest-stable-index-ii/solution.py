# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        velqanidor = (nums, k)
        suffix_minimum = [0] * len(nums)
        suffix_minimum[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_minimum[i] = min(nums[i], suffix_minimum[i + 1])

        prefix_maximum = nums[0]
        for i, value in enumerate(nums):
            prefix_maximum = max(prefix_maximum, value)
            if prefix_maximum - suffix_minimum[i] <= velqanidor[1]:
                return i
        return -1
