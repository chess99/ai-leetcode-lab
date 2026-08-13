# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:22:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def first_digit(num: int) -> int:
            while num >= 10:
                num //= 10
            return num

        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        result = 0
        for i in range(len(nums)):
            first = first_digit(nums[i])
            for j in range(i + 1, len(nums)):
                if gcd(first, nums[j] % 10) == 1:
                    result += 1

        return result
