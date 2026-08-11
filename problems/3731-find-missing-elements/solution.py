# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:15:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        values = set(nums)
        return [value for value in range(min(nums), max(nums) + 1) if value not in values]
