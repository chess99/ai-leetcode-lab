# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:04:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        def is_prime(value: int) -> bool:
            if value < 2:
                return False
            divisor = 2
            while divisor * divisor <= value:
                if value % divisor == 0:
                    return False
                divisor += 1
            return True

        return any(is_prime(count) for count in counts.values())
