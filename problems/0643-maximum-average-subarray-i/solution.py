# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:51:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        maximum = window
        for index in range(k, len(nums)):
            window += nums[index] - nums[index - k]
            maximum = max(maximum, window)
        return maximum / k
