# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = best = 1
        for a, b in zip(nums, nums[1:]):
            inc = inc + 1 if b > a else 1
            dec = dec + 1 if b < a else 1
            best = max(best, inc, dec)
        return best
