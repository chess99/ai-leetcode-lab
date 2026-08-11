# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
from functools import cache
from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        modulo = 1_000_000_007

        @cache
        def count(mask: int, last: int) -> int:
            if mask == (1 << len(nums)) - 1:
                return 1
            total = 0
            for nxt in range(len(nums)):
                if mask >> nxt & 1:
                    continue
                if nums[last] % nums[nxt] == 0 or nums[nxt] % nums[last] == 0:
                    total += count(mask | (1 << nxt), nxt)
            return total % modulo

        return sum(count(1 << start, start) for start in range(len(nums))) % modulo
