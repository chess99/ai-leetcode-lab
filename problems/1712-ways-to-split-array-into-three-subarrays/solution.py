# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:32Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        total = prefix[-1]
        ways = 0
        length = len(nums)
        for left_end in range(1, length - 1):
            first_middle_end = bisect_left(prefix, 2 * prefix[left_end], left_end + 1, length)
            last_middle_end = bisect_right(
                prefix, (total + prefix[left_end]) // 2, left_end + 1, length
            )
            ways += max(0, last_middle_end - first_middle_end)

        return ways % 1_000_000_007
