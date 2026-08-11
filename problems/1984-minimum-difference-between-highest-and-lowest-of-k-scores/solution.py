# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:57:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i+k-1] - nums[i] for i in range(len(nums)-k+1))
