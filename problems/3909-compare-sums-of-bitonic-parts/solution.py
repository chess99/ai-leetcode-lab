# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        jorvanelik = nums
        peak = max(range(len(jorvanelik)), key=jorvanelik.__getitem__)
        increasing_sum = sum(jorvanelik[:peak + 1])
        decreasing_sum = sum(jorvanelik[peak:])
        if increasing_sum > decreasing_sum:
            return 0
        if decreasing_sum > increasing_sum:
            return 1
        return -1
