# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:45Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        mod = 1_000_000_007
        lower = []
        upper = []
        lower_sum = upper_sum = 0
        answer = []

        for index, number in enumerate(nums):
            value = number - index
            if not lower or value <= -lower[0]:
                heapq.heappush(lower, -value)
                lower_sum += value
            else:
                heapq.heappush(upper, value)
                upper_sum += value

            if len(lower) > len(upper) + 1:
                moved = -heapq.heappop(lower)
                lower_sum -= moved
                heapq.heappush(upper, moved)
                upper_sum += moved
            elif len(lower) < len(upper):
                moved = heapq.heappop(upper)
                upper_sum -= moved
                heapq.heappush(lower, -moved)
                lower_sum += moved

            median = -lower[0]
            moves = median * len(lower) - lower_sum
            moves += upper_sum - median * len(upper)
            answer.append(moves % mod)
        return answer
