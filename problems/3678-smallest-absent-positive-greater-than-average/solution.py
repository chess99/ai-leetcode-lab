# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:08:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        present = set(nums)
        candidate = sum(nums) // len(nums) + 1
        candidate = max(candidate, 1)
        while candidate in present:
            candidate += 1
        return candidate
