# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        modulus = 10 ** 9 + 7
        counts = [0] * 31
        for value in nums:
            for bit in range(31):
                counts[bit] += value >> bit & 1
        answer = 0
        for _ in range(k):
            value = 0
            for bit in range(31):
                if counts[bit]:
                    value |= 1 << bit
                    counts[bit] -= 1
            answer = (answer + value * value) % modulus
        return answer
