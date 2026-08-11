# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:23:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts={}
        for value in nums:counts[value]=counts.get(value,0)+1
        return sum(value for value,count in counts.items() if count==1)
