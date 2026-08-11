# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        best_with_player = [0] * len(players)

        for current, (_, score) in enumerate(players):
            best_with_player[current] = score
            for previous in range(current):
                if players[previous][1] <= score:
                    best_with_player[current] = max(
                        best_with_player[current], best_with_player[previous] + score
                    )

        return max(best_with_player)
