# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:06Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        size = len(stones)
        if (size - 1) % (k - 1):
            return -1
        prefix = [0]
        for stone in stones:
            prefix.append(prefix[-1] + stone)

        @lru_cache(None)
        def cost(left, right, piles):
            length = right - left
            if length == piles:
                return 0
            if length < piles or (length - piles) % (k - 1):
                return float('inf')
            if piles == 1:
                return cost(left, right, k) + prefix[right] - prefix[left]
            return min(cost(left, middle, 1) + cost(middle, right, piles - 1)
                       for middle in range(left + 1, right, k - 1))

        return cost(0, size, 1)
