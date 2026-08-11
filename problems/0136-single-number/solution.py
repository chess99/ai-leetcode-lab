# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:18:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for number in nums:
            result ^= number
        return result
