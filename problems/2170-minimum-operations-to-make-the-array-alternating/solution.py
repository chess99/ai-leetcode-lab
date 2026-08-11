# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:30Z
# Experiment: ai-leetcode-lab, round 1

from collections import Counter
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even_counts = Counter(nums[::2]).most_common(2) + [(None, 0)]
        odd_counts = Counter(nums[1::2]).most_common(2) + [(None, 0)]

        if even_counts[0][0] != odd_counts[0][0]:
            return len(nums) - even_counts[0][1] - odd_counts[0][1]

        return min(
            len(nums) - even_counts[0][1] - odd_counts[1][1],
            len(nums) - even_counts[1][1] - odd_counts[0][1],
        )
