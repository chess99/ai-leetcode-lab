# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:31:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        return max(a ^ b for a in nums for b in nums if abs(a - b) <= min(a, b))
