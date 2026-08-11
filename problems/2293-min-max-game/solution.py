# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:24:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [min(nums[i], nums[i+1]) if (i//2) % 2 == 0 else max(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]
        return nums[0]
