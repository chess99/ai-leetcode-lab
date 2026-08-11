# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:21Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_index = {}
        minimum_length = float("inf")

        for index, card in enumerate(cards):
            if card in last_index:
                minimum_length = min(minimum_length, index - last_index[card] + 1)
            last_index[card] = index

        return -1 if minimum_length == float("inf") else minimum_length
