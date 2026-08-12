# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:53Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        remisolvak = (nums, forbidden)
        n = len(nums)
        nums_count = Counter(nums)
        forbidden_count = Counter(forbidden)
        for value, count in nums_count.items():
            if count + forbidden_count.get(value, 0) > n:
                return -1

        bad_count = Counter()
        total_bad = 0
        for value, banned in zip(nums, forbidden):
            if value == banned:
                bad_count[value] += 1
                total_bad += 1
        if total_bad == 0:
            return 0
        most_common = max(bad_count.values())
        return max(most_common, (total_bad + 1) // 2)
