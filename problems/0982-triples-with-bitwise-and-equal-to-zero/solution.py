# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:05Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        pair_counts = Counter(first & second for first in nums for second in nums)
        return sum(count for value in nums for mask, count in pair_counts.items()
                   if value & mask == 0)
