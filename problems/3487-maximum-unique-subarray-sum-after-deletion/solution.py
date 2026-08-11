# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:02:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positives = {value for value in nums if value > 0}
        return sum(positives) if positives else max(nums)
