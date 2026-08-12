# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total = n * (n + 1) // 2
        if k > total:
            return -1

        def active(time):
            marked = [False] * n
            for i in range(time + 1):
                marked[order[i]] = True
            invalid = 0
            run = 0
            for is_marked in marked:
                if is_marked:
                    invalid += run * (run + 1) // 2
                    run = 0
                else:
                    run += 1
            invalid += run * (run + 1) // 2
            return total - invalid >= k

        left, right = 0, n - 1
        if not active(right):
            return -1
        while left < right:
            middle = (left + right) // 2
            if active(middle):
                right = middle
            else:
                left = middle + 1
        return left
