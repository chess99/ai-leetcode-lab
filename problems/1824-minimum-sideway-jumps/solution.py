# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        costs=[1,0,1]
        for obstacle in obstacles:
            if obstacle:costs[obstacle-1]=float('inf')
            best=min(costs)
            for lane in range(3):
                if lane!=obstacle-1:costs[lane]=min(costs[lane],best+1)
        return min(costs)
