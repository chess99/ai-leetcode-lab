# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:30:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        for left in range(len(nums)):
            distinct = set()
            for right in range(left, len(nums)):
                distinct.add(nums[right])
                result += len(distinct) ** 2

        return result
