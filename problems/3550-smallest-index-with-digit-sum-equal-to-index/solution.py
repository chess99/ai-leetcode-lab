# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:04:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index, value in enumerate(nums):
            if sum(map(int, str(value))) == index:
                return index
        return -1
