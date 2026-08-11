# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:27:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        result = 0
        while left < right:
            if nums[left] + nums[right] <= target:
                result += right - left
                left += 1
            else:
                right -= 1
        return result % 1_000_000_007
