# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:05:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        values=set(nums)
        while original in values:original*=2
        return original
