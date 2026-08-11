# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:58:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        selected = []
        current = 0
        for value in sorted(nums, reverse=True):
            selected.append(value)
            current += value
            if current > total - current:
                return selected
