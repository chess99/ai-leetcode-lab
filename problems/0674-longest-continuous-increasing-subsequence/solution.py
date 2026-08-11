# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:57:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        best = current = 1
        for i in range(1, len(nums)):
            current = current + 1 if nums[i] > nums[i - 1] else 1
            best = max(best, current)
        return best
