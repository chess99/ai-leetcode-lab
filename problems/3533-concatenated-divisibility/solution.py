# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:19Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List


class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        order = sorted(range(n), key=lambda index: (nums[index], index))
        powers = [pow(10, len(str(value)), k) for value in nums]
        full = (1 << n) - 1

        @lru_cache(None)
        def can(mask: int, remainder: int) -> bool:
            if mask == full:
                return remainder == 0
            previous_value = None
            for index in order:
                if mask >> index & 1 or nums[index] == previous_value:
                    continue
                previous_value = nums[index]
                next_remainder = (remainder * powers[index] + nums[index]) % k
                if can(mask | (1 << index), next_remainder):
                    return True
            return False

        if not can(0, 0):
            return []
        answer = []
        mask = remainder = 0
        for _ in range(n):
            for index in order:
                if mask >> index & 1:
                    continue
                next_remainder = (remainder * powers[index] + nums[index]) % k
                if can(mask | (1 << index), next_remainder):
                    answer.append(nums[index])
                    mask |= 1 << index
                    remainder = next_remainder
                    break
        return answer
