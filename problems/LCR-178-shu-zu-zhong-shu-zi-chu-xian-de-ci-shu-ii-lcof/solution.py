# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        ones = twos = 0
        for action in actions:
            ones = (ones ^ action) & ~twos
            twos = (twos ^ action) & ~ones
        return ones
