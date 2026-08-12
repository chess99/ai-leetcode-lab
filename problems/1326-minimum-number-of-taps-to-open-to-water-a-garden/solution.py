# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        reach=[0]*(n+1)
        for center,radius in enumerate(ranges):
            left=max(0,center-radius);reach[left]=max(reach[left],min(n,center+radius))
        taps=0;current=next_end=0
        for point in range(n):
            next_end=max(next_end,reach[point])
            if point==current:
                if next_end<=point:return -1
                taps+=1;current=next_end
        return taps
