# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:51:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        combined = 0
        for value in nums:
            combined |= value
        return combined << (len(nums) - 1)
