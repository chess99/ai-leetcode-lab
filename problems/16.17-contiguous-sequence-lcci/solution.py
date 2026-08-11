# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:01:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = current = nums[0]
        for value in nums[1:]:
            current = max(value, current + value)
            best = max(best, current)
        return best
