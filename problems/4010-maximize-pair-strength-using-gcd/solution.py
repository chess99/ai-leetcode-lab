# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:24:21Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        return max(nums[i]*nums[j]//gcd(nums[i],nums[j])**2 for i in range(len(nums)) for j in range(i))
