# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        people_by_hat = [[] for _ in range(41)]
        for person, choices in enumerate(hats):
            for hat in choices:
                people_by_hat[hat].append(person)
        full = (1 << len(hats)) - 1
        dp = [0] * (full + 1)
        dp[0] = 1
        for people in people_by_hat:
            following = dp[:]
            for mask, ways in enumerate(dp):
                if not ways:
                    continue
                for person in people:
                    bit = 1 << person
                    if mask & bit == 0:
                        following[mask | bit] += ways
            dp = [ways % 1_000_000_007 for ways in following]
        return dp[full]
