# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        from collections import deque
        q=deque();best=-10**20
        for x,y in points:
            while q and x-q[0][0]>k:q.popleft()
            if q:best=max(best,x+y+q[0][1])
            while q and q[-1][1]<=y-x:q.pop()
            q.append((x,y-x))
        return best
