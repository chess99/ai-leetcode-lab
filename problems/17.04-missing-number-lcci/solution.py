# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:01:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for index, value in enumerate(nums):
            missing ^= index ^ value
        return missing
