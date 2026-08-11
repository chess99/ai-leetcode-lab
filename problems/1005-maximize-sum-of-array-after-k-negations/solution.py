# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:15:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if k and nums[i] < 0: nums[i] = -nums[i]; k -= 1
        return sum(nums) - (min(nums) * 2 if k % 2 else 0)
