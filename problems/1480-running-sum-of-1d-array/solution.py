# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:03:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for index in range(1, len(nums)):
            nums[index] += nums[index - 1]
        return nums
