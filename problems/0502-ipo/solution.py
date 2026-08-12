# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:18Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        available = []
        index = 0
        for _ in range(k):
            while index < len(projects) and projects[index][0] <= w:
                heapq.heappush(available, -projects[index][1])
                index += 1
            if not available:
                break
            w -= heapq.heappop(available)
        return w
