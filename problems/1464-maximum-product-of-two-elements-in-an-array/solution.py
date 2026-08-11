# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:03:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = sorted(nums)[-2:]
        return (first - 1) * (second - 1)
