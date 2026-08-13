# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort();return len({nums[i]+nums[-i-1] for i in range(len(nums)//2)})
