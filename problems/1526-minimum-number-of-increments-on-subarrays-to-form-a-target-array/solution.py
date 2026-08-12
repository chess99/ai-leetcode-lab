# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:59Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return target[0] + sum(max(0, current - previous) for previous, current in zip(target, target[1:]))
