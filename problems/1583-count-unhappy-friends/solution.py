# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank=[[0]*n for _ in range(n)]; partner=[0]*n
        for person, order in enumerate(preferences):
            for place, other in enumerate(order):rank[person][other]=place
        for a,b in pairs:partner[a]=b;partner[b]=a
        return sum(any(u != x and rank[x][u]<rank[x][partner[x]] and rank[u][x]<rank[u][partner[u]] for u in range(n)) for x in range(n))
