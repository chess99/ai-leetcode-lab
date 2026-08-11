# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        best = len(nums) + 1
        for i in range(len(nums)):
            value = 0
            for j in range(i, len(nums)):
                value |= nums[j]
                if value >= k:
                    best = min(best, j - i + 1)
                    break
        return best if best <= len(nums) else -1
