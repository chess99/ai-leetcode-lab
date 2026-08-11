# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        counts = Counter(nums)
        for start in sorted(counts):
            needed = counts[start]
            if needed == 0:
                continue
            for value in range(start, start + k):
                if counts[value] < needed:
                    return False
                counts[value] -= needed
        return True
