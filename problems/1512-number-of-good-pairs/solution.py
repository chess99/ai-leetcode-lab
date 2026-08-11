# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:07:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}; result = 0
        for value in nums:
            result += counts.get(value, 0)
            counts[value] = counts.get(value, 0) + 1
        return result
