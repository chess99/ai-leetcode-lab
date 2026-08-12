# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:12Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from math import gcd
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        frequencies = Counter()
        answer = 0
        for value in nums:
            common = gcd(value, k)
            for previous, count in frequencies.items():
                if common * previous % k == 0:
                    answer += count
            frequencies[common] += 1
        return answer
