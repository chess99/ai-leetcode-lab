# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        banned={front for front,back in zip(fronts,backs) if front==back}
        candidates=set(fronts+backs)-banned
        return min(candidates) if candidates else 0
