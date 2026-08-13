# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:26:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        return len(set(scores))
