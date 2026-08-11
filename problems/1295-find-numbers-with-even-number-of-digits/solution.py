# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:46:01Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(value))%2==0 for value in nums)
