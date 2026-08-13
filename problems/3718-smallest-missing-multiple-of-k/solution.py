# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:15:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        values = set(nums)
        multiple = k
        while multiple in values:
            multiple += k
        return multiple
