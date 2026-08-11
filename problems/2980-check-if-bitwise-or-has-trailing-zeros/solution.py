# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return sum(value % 2 == 0 for value in nums) >= 2
