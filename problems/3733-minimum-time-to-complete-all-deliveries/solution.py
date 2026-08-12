# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:51Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        faronthic = (d, r)
        lcm = r[0] // gcd(r[0], r[1]) * r[1]
        def feasible(time):
            available0 = time - time // r[0]
            available1 = time - time // r[1]
            either = time - time // lcm
            return available0 >= d[0] and available1 >= d[1] and either >= d[0] + d[1]
        left, right = 0, 2 * sum(d) + 10
        while not feasible(right): right *= 2
        while left < right:
            mid = (left + right) // 2
            if feasible(mid): right = mid
            else: left = mid + 1
        return left
