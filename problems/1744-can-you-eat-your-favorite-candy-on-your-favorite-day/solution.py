# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix=[0]
        for count in candiesCount:prefix.append(prefix[-1]+count)
        return [prefix[t]<=(d+1)*cap and prefix[t+1]>d for t,d,cap in queries]
