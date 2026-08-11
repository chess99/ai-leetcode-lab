# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def feasible(gap: int) -> bool:
            count, last = 1, price[0]
            for value in price[1:]:
                if value - last >= gap:
                    count += 1
                    last = value
            return count >= k
        lo, hi = 0, price[-1] - price[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid): lo = mid
            else: hi = mid - 1
        return lo
