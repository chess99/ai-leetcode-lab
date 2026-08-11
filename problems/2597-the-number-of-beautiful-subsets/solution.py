# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        total = 1
        for remainder in range(k):
            values = sorted(value for value in counts if value % k == remainder)
            skip, take, previous = 1, 0, None
            for value in values:
                choices = (1 << counts[value]) - 1
                if previous is not None and value - previous == k:
                    skip, take = skip + take, skip * choices
                else:
                    skip, take = skip + take, (skip + take) * choices
                previous = value
            total *= skip + take
        return total - 1
