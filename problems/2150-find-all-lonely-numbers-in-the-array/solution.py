# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:28Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return [
            number
            for number, count in counts.items()
            if count == 1 and number - 1 not in counts and number + 1 not in counts
        ]
