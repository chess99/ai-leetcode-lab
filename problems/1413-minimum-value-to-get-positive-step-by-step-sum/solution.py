# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:58:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = lowest = 0
        for value in nums:
            prefix += value
            lowest = min(lowest, prefix)
        return 1 - lowest
