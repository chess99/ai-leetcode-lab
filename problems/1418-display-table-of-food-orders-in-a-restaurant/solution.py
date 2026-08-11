# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:31Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter, defaultdict
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        counts = defaultdict(Counter)
        foods = set()
        for _, table, food in orders:
            counts[table][food] += 1
            foods.add(food)
        sorted_foods = sorted(foods)
        return [["Table"] + sorted_foods] + [[table] + [str(counts[table][food]) for food in sorted_foods] for table in sorted(counts, key=int)]
