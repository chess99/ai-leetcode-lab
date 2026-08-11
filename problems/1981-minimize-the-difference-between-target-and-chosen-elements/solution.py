# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        sums={0}
        for row in mat:sums={total+value for total in sums for value in row if total+value<=target+70}
        return min(abs(total-target) for total in sums)
