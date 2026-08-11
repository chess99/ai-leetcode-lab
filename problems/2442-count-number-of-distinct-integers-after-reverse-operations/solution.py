# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set(nums) | {int(str(x)[::-1]) for x in nums})
