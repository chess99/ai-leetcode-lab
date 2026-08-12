# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1]);on=set()
        for a,b,d in tasks:
            have=sum(x in on for x in range(a,b+1))
            for x in range(b,a-1,-1):
                if have>=d:break
                if x not in on:on.add(x);have+=1
        return len(on)
