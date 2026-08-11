# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:24:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        middle = nums[len(nums) // 2]
        return nums.count(middle) == 1
