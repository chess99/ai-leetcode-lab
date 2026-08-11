# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:05:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countElements(self, nums: List[int]) -> int:
        low,high=min(nums),max(nums);return sum(low<value<high for value in nums)
