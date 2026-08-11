# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:37:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current = best = nums[0]
        for index in range(1, len(nums)):
            current = current + nums[index] if nums[index] > nums[index - 1] else nums[index]
            best = max(best, current)
        return best
