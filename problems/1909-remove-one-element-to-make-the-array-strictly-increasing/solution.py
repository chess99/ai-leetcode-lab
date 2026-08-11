# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:51:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                if removed: return False
                removed = True
                if i > 1 and nums[i] <= nums[i-2]: nums[i] = nums[i-1]
        return True
