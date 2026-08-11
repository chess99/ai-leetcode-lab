# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        rows = []
        counts = defaultdict(int)
        for value in nums:
            row = counts[value]
            if row == len(rows):
                rows.append([])
            rows[row].append(value)
            counts[value] += 1
        return rows
