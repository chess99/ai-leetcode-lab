# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:47:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_sum = sum(value for value in nums if value < 10)
        double_digit_sum = sum(nums) - single_digit_sum
        return single_digit_sum != double_digit_sum
