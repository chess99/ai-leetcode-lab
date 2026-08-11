# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:07Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        key_counts = defaultdict(int)
        bad_pairs = 0

        for index, number in enumerate(nums):
            key = number - index
            bad_pairs += index - key_counts[key]
            key_counts[key] += 1

        return bad_pairs
