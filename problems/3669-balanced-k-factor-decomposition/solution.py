# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:45Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        best = [1] * (k - 1) + [n]
        best_diff = n - 1

        def search(remain: int, parts: int, lower: int, chosen: List[int]) -> None:
            nonlocal best, best_diff
            if parts == 1:
                if remain < lower:
                    return
                candidate = chosen + [remain]
                difference = candidate[-1] - candidate[0]
                if difference < best_diff:
                    best_diff = difference
                    best = candidate
                return

            divisor = lower
            while divisor ** parts <= remain:
                if remain % divisor == 0:
                    search(remain // divisor, parts - 1, divisor, chosen + [divisor])
                divisor += 1

        search(n, k, 1, [])
        return best
