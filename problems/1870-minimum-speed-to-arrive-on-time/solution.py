# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:37Z
# Experiment: ai-leetcode-lab, round 1
from math import ceil
from typing import List
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour<=len(dist)-1:return -1
        def ok(speed):return sum(ceil(d/speed) for d in dist[:-1])+dist[-1]/speed<=hour
        low,high=1,10**7
        while low<high:
            mid=(low+high)//2
            if ok(mid):high=mid
            else:low=mid+1
        return low if ok(low) else -1
