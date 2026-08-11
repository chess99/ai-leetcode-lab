# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:51:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort();return nums[-1]*nums[-2]-nums[0]*nums[1]
