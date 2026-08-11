# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:31:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[index] > nums[(index + 1) % len(nums)] for index in range(len(nums))) <= 1
