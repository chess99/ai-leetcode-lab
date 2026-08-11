# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:18:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = {}
        for value in nums:
            counts[value] = counts.get(value, 0) + 1
        return sorted(nums, key=lambda value: (counts[value], -value))
