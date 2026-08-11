# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:56Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod=1_000_000_007; seen=ans=0
        for count in Counter(y for _,y in points).values():
            pairs=count*(count-1)//2; ans=(ans+seen*pairs)%mod; seen+=pairs
        return ans
