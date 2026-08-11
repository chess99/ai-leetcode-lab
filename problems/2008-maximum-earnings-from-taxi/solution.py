# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        starting_at = [[] for _ in range(n + 1)]
        for start, end, tip in rides:
            starting_at[start].append((end, tip))

        earnings = [0] * (n + 1)
        for place in range(1, n + 1):
            earnings[place] = max(earnings[place], earnings[place - 1])
            for end, tip in starting_at[place]:
                earnings[end] = max(
                    earnings[end], earnings[place] + end - place + tip
                )

        return earnings[n]
