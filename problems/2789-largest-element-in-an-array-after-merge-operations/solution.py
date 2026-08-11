# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        total=nums[-1]
        for x in reversed(nums[:-1]): total=total+x if x<=total else total
        return total
