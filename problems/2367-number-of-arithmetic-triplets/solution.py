# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:58:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        values = set(nums)
        return sum(value + diff in values and value + 2 * diff in values for value in nums)
