# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:55Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for value in nums:
            index = abs(value) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [i + 1 for i, value in enumerate(nums) if value > 0]
