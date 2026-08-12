# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:16:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        by_value = {}
        best = [0] * (k + 1)
        for value in nums:
            ending = by_value.setdefault(value, [0] * (k + 1))
            for changes in range(k, -1, -1):
                candidate = ending[changes] + 1
                if changes:
                    candidate = max(candidate, best[changes - 1] + 1)
                ending[changes] = candidate
                best[changes] = max(best[changes], candidate)
        return best[k]
