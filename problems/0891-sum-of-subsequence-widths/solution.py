# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort();mod=10**9+7;n=len(nums);return sum((x-y)*(pow(2,i,mod))for i,(x,y)in enumerate(zip(nums,nums[::-1])))%mod
