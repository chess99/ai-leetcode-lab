# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        maximum = max(nums)
        frequency = [0] * (maximum + 1)
        for value in nums:
            frequency[value] += 1
        prefix = [0] * (maximum + 1)
        for value in range(1, maximum + 1):
            prefix[value] = prefix[value - 1] + frequency[value]
        answer = 0
        for denominator in range(1, maximum + 1):
            if frequency[denominator] == 0:
                continue
            quotient = 1
            for left in range(denominator, maximum + 1, denominator):
                right = min(maximum, left + denominator - 1)
                count = prefix[right] - prefix[left - 1]
                answer += frequency[denominator] * quotient * count
                quotient += 1
        return answer % 1_000_000_007
