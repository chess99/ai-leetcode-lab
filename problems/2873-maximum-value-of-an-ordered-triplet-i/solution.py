# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:30:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_prefix = nums[0]
        max_difference = 0
        result = 0

        for num in nums[1:]:
            result = max(result, max_difference * num)
            max_difference = max(max_difference, max_prefix - num)
            max_prefix = max(max_prefix, num)

        return result
