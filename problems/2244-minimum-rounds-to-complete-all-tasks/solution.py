# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:19Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0

        for count in Counter(tasks).values():
            if count == 1:
                return -1
            rounds += (count + 2) // 3

        return rounds
