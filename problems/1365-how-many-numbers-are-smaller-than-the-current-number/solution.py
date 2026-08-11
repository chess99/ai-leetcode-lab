# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:53:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        first = {}
        for i, value in enumerate(sorted_nums): first.setdefault(value, i)
        return [first[value] for value in nums]
