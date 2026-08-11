# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:24:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def digit_range(number: int) -> int:
            digits = [int(digit) for digit in str(number)]
            return max(digits) - min(digits)

        ranges = [digit_range(number) for number in nums]
        maximum = max(ranges)
        return sum(number for number, value_range in zip(nums, ranges) if value_range == maximum)
