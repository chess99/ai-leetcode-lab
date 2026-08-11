# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:21Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        root = {}
        distinct = 0

        for start in range(len(nums)):
            node = root
            divisible = 0
            for value in nums[start:]:
                if value % p == 0:
                    divisible += 1
                if divisible > k:
                    break
                if value not in node:
                    node[value] = {}
                    distinct += 1
                node = node[value]

        return distinct
