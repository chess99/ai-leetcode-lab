# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
import heapq
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        choices=[]
        for row,limit in zip(grid,limits): choices.extend(heapq.nlargest(limit,row))
        return sum(heapq.nlargest(k,choices))
