# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        positions=set(nums)
        for a,b in zip(moveFrom,moveTo): positions.discard(a); positions.add(b)
        return sorted(positions)
