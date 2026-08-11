# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:24:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return min(nums, key=lambda value: (abs(value), -value))
