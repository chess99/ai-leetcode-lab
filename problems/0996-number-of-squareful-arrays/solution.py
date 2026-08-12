# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:06Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from math import isqrt
from typing import List


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        counts = Counter(nums)
        values = list(counts)
        compatible = {value: [following for following in values
                              if isqrt(value + following) ** 2 == value + following]
                      for value in values}

        def search(previous, remaining):
            if remaining == 0:
                return 1
            answer = 0
            for value in compatible[previous]:
                if counts[value]:
                    counts[value] -= 1
                    answer += search(value, remaining - 1)
                    counts[value] += 1
            return answer

        answer = 0
        for value in values:
            counts[value] -= 1
            answer += search(value, len(nums) - 1)
            counts[value] += 1
        return answer
