# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:02:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even_count = sum(num % 2 == 0 for num in nums)
        return [0] * even_count + [1] * (len(nums) - even_count)
