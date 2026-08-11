# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:31:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        best = float('inf')
        for j in range(1, len(nums)-1):
            for i in range(j):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]: best = min(best, nums[i]+nums[j]+nums[k])
        return best if best < float('inf') else -1
