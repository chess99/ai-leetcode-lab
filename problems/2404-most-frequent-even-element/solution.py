# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:59:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts={}
        for value in nums:
            if value%2==0:counts[value]=counts.get(value,0)+1
        return min(counts,key=lambda value:(-counts[value],value)) if counts else -1
