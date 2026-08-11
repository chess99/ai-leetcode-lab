# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:52:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        return sum(nums[a]+nums[b]+nums[c]==nums[d] for a in range(len(nums)) for b in range(a+1,len(nums)) for c in range(b+1,len(nums)) for d in range(c+1,len(nums)))
