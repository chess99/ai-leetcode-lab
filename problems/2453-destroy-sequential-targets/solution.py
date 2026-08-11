# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:19Z
# Experiment: ai-leetcode-lab, round 1

from collections import Counter
from typing import List


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        counts = Counter(num % space for num in nums)
        best_count = max(counts.values())
        return min(num for num in nums if counts[num % space] == best_count)
