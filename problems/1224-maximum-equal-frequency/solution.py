# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:12Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        value_frequency = Counter()
        frequency_count = Counter()
        maximum = answer = 0
        for length, value in enumerate(nums, 1):
            old = value_frequency[value]
            if old:
                frequency_count[old] -= 1
            current = old + 1
            value_frequency[value] = current
            frequency_count[current] += 1
            maximum = max(maximum, current)

            if maximum == 1:
                answer = length
            elif (frequency_count[1] == 1 and
                  maximum * frequency_count[maximum] + 1 == length):
                answer = length
            elif (frequency_count[maximum] == 1 and
                  (maximum - 1) * (frequency_count[maximum - 1] + 1)
                  == length - 1):
                answer = length
        return answer
