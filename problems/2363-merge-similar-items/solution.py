# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:58:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        totals = defaultdict(int)
        for value, weight in items1 + items2: totals[value] += weight
        return [[value, totals[value]] for value in sorted(totals)]
