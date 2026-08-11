# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        seen=defaultdict(int); answer=0
        for x,y in coordinates:
            for dx in range(k+1): answer+=seen[(x^dx,y^(k-dx))]
            seen[(x,y)]+=1
        return answer
