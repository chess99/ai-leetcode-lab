# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:21Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prices = []
        best_beauty = []
        maximum = 0

        for price, beauty in items:
            maximum = max(maximum, beauty)
            prices.append(price)
            best_beauty.append(maximum)

        answer = []
        for query in queries:
            index = bisect_right(prices, query) - 1
            answer.append(best_beauty[index] if index >= 0 else 0)
        return answer
