# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        largest = max(milestones)
        remaining = total - largest
        return total if largest <= remaining + 1 else 2 * remaining + 1
