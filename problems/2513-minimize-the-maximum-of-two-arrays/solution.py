# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lcm = divisor1 // gcd(divisor1, divisor2) * divisor2
        def possible(limit: int) -> bool:
            return (limit - limit // divisor1 >= uniqueCnt1 and
                    limit - limit // divisor2 >= uniqueCnt2 and
                    limit - limit // lcm >= uniqueCnt1 + uniqueCnt2)
        lo, hi = 1, 10**18
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid): hi = mid
            else: lo = mid + 1
        return lo
