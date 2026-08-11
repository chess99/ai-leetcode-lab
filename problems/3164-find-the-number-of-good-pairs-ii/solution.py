# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        counts = Counter(nums1)
        maximum = max(nums1)
        answer = 0
        for value, frequency in Counter(nums2).items():
            divisor = value * k
            for multiple in range(divisor, maximum + 1, divisor):
                answer += frequency * counts[multiple]
        return answer
