# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length = len(nums)
        frequency_difference = [0] * (length + 1)
        for start, end in requests:
            frequency_difference[start] += 1
            frequency_difference[end + 1] -= 1

        frequencies = []
        current_frequency = 0
        for index in range(length):
            current_frequency += frequency_difference[index]
            frequencies.append(current_frequency)

        nums.sort()
        frequencies.sort()
        modulo = 1_000_000_007
        return sum(value * frequency for value, frequency in zip(nums, frequencies)) % modulo
