# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:39Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List

class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        minaveloru = nums
        frequencies = Counter(minaveloru)
        frequency_counts = Counter(frequencies.values())
        for value in minaveloru:
            if frequency_counts[frequencies[value]] == 1:
                return value
        return -1
