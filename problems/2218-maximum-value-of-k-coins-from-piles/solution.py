# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dynamic = [0] + [-1] * k
        for pile in piles:
            prefix = [0]
            for value in pile[:k]:
                prefix.append(prefix[-1] + value)
            updated = dynamic[:]
            for used in range(k + 1):
                if dynamic[used] < 0:
                    continue
                for take in range(1, min(len(prefix) - 1, k - used) + 1):
                    updated[used + take] = max(
                        updated[used + take], dynamic[used] + prefix[take]
                    )
            dynamic = updated
        return dynamic[k]
