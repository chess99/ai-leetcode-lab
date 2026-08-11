# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:06:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for value in range(len(nums)+1):
            if sum(number>=value for number in nums)==value:return value
        return -1
