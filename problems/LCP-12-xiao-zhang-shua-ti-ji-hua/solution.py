# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        def days(limit):
            used = 1; total = biggest = 0
            for value in time:
                total += value; biggest = max(biggest, value)
                if total - biggest > limit:
                    used += 1; total = biggest = value
            return used
        lo, hi = 0, sum(time)
        while lo < hi:
            mid = (lo + hi) // 2
            if days(mid) <= m: hi = mid
            else: lo = mid + 1
        return lo
