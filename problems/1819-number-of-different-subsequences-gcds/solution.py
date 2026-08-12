# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:46Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        maximum = max(nums)
        present = [False] * (maximum + 1)
        for value in nums:
            present[value] = True
        answer = 0
        for candidate in range(1, maximum + 1):
            common = 0
            for multiple in range(candidate, maximum + 1, candidate):
                if present[multiple]:
                    common = gcd(common, multiple)
                    if common == candidate:
                        answer += 1
                        break
        return answer
