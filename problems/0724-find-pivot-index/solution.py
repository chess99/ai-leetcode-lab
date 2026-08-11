# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:02:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i, value in enumerate(nums):
            if left == total - left - value:
                return i
            left += value
        return -1
