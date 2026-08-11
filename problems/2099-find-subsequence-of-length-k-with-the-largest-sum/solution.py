# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:03:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        selected={index for _,index in sorted((value,index) for index,value in enumerate(nums))[-k:]};return [value for index,value in enumerate(nums) if index in selected]
