# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:31:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        return sum((sum(value >> bit & 1 for value in nums) >= k) << bit for bit in range(32))
