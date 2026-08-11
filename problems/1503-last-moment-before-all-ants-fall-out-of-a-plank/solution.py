# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:54:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(left, default=0) if not right else max(max(left, default=0), n - min(right))
