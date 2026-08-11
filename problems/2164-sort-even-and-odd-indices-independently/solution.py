# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:18:02Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = iter(sorted(nums[::2]))
        odd = iter(sorted(nums[1::2], reverse=True))
        return [next(even) if index % 2 == 0 else next(odd) for index in range(len(nums))]
