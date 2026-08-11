# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:06:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(digit) for value in nums for digit in str(value)]
