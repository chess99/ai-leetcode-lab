# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:03:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        smallest = nums[0]
        best = -1
        for value in nums[1:]:
            if value > smallest:
                best = max(best, value - smallest)
            smallest = min(smallest, value)
        return best
