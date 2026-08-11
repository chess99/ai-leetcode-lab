# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:24:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        return sorted(nums) == list(range(1, n)) + [n - 1]
