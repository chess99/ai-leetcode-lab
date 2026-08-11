# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def best(intervals: List[List[int]]) -> int:
            intervals.sort()
            total = answer = 0
            right = 0
            for left_index, (left, end, value) in enumerate(intervals):
                limit = left + k
                while right < len(intervals) and intervals[right][1] < limit:
                    a, b, coins_per_bag = intervals[right]
                    total += (b - a + 1) * coins_per_bag
                    right += 1
                partial = 0
                if right < len(intervals):
                    a, _, coins_per_bag = intervals[right]
                    partial = max(0, limit - a) * coins_per_bag
                answer = max(answer, total + partial)
                if left_index < right:
                    total -= (end - left + 1) * value
            return answer

        forward = [segment[:] for segment in coins]
        backward = [[-right, -left, value] for left, right, value in coins]
        return max(best(forward), best(backward))
