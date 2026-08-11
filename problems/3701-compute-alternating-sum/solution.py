# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:08:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(num if index % 2 == 0 else -num for index, num in enumerate(nums))
