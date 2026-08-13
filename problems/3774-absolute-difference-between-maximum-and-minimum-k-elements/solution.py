# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:15:59Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return abs(sum(nums[-k:]) - sum(nums[:k]))
