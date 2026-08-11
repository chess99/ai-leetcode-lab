# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:05:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        return sum(nums[i]==nums[j] and i*j%k==0 for i in range(len(nums)) for j in range(i+1,len(nums)))
