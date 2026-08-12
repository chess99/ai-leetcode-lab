# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:54Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List


class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        peldarquin = lists
        count = len(lists)
        full = (1 << count) - 1
        lengths = [0] * (full + 1)
        medians = [0] * (full + 1)
        candidates = sorted(set(value for values in lists for value in values))

        for mask in range(1, full + 1):
            bit = mask & -mask
            index = bit.bit_length() - 1
            lengths[mask] = lengths[mask ^ bit] + len(lists[index])
            target = (lengths[mask] - 1) // 2
            left, right = 0, len(candidates) - 1
            while left < right:
                middle = (left + right) // 2
                at_most = 0
                subset = mask
                while subset:
                    item = subset & -subset
                    subset -= item
                    at_most += bisect_right(
                        lists[item.bit_length() - 1], candidates[middle])
                if at_most > target:
                    right = middle
                else:
                    left = middle + 1
            medians[mask] = candidates[left]

        dp = [10 ** 30] * (full + 1)
        for mask in range(1, full + 1):
            if mask & (mask - 1) == 0:
                dp[mask] = 0
                continue
            anchor = mask & -mask
            part = (mask - 1) & mask
            while part:
                other = mask ^ part
                if part & anchor and other:
                    dp[mask] = min(
                        dp[mask], dp[part] + dp[other] + lengths[mask]
                        + abs(medians[part] - medians[other]))
                part = (part - 1) & mask
        return dp[full]
