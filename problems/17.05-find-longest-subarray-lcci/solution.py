# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        first = {0: -1}
        balance = 0
        best_start = best_length = 0
        for index, value in enumerate(array):
            balance += 1 if value[0].isdigit() else -1
            if balance in first:
                start = first[balance] + 1
                length = index - first[balance]
                if length > best_length:
                    best_start, best_length = start, length
            else:
                first[balance] = index
        return array[best_start:best_start + best_length]
