# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:55:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        from math import gcd
        return gcd(min(nums), max(nums))
