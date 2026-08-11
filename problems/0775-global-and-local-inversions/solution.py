# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:43:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(value - index) <= 1 for index, value in enumerate(nums))
