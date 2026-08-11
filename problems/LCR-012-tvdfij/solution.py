# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:32:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for index, value in enumerate(nums):
            if left_sum == total - left_sum - value:
                return index
            left_sum += value
        return -1
