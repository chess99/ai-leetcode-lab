# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:10:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all(a <= b for a, b in zip(nums, nums[1:])) or all(a >= b for a, b in zip(nums, nums[1:]))
