# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse=True)
        profit = 0
        categories = set()
        duplicates = []
        for value, category in items[:k]:
            profit += value
            if category in categories:
                duplicates.append(value)
            else:
                categories.add(category)
        answer = profit + len(categories) ** 2
        for value, category in items[k:]:
            if category in categories or not duplicates:
                continue
            profit += value - duplicates.pop()
            categories.add(category)
            answer = max(answer, profit + len(categories) ** 2)
        return answer
