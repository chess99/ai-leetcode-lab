# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        forbidden = set(banned)
        total = count = 0
        for value in range(1, n + 1):
            if value in forbidden:
                continue
            if total + value > maxSum:
                break
            total += value
            count += 1
        return count
