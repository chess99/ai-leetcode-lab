# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:58:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = sum(nums.count(value) // 2 for value in set(nums))
        return [pairs, len(nums) - 2 * pairs]
