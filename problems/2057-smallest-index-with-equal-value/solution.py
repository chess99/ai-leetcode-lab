# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:05:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        return next((i for i, value in enumerate(nums) if i % 10 == value), -1)
