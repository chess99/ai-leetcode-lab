# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        low,high=bounds[0]
        delta=0
        for i in range(1,len(original)):
            delta+=original[i]-original[i-1]
            low=max(low,bounds[i][0]-delta); high=min(high,bounds[i][1]-delta)
        return max(0,high-low+1)
