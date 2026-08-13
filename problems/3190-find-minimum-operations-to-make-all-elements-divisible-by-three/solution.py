# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:47:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(num % 3 != 0 for num in nums)
