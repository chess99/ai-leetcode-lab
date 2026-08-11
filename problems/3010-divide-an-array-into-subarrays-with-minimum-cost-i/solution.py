# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0]+sum(sorted(nums[1:])[:2])
