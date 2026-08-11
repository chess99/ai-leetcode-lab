# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:25:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        drop = next((i for i in range(len(nums) - 1) if nums[i] > nums[i + 1]), -1)
        if drop < 0:
            return 0
        if nums[-1] > nums[0] or any(nums[i] > nums[i + 1] for i in range(drop + 1, len(nums) - 1)):
            return -1
        return len(nums) - drop - 1
