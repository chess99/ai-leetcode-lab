# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        available = 0
        groups = 0
        for limit in sorted(usageLimits):
            available += limit
            if available >= groups + 1:
                groups += 1
                available -= groups
        return groups
