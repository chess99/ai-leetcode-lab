# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:05:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(sum(value < 0 for value in nums), sum(value > 0 for value in nums))
