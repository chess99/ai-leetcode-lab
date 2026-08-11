# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def matches(slot: str, candidate: str) -> bool:
            return (len(slot) == len(candidate)
                    and all(cell == " " or cell == char
                            for cell, char in zip(slot, candidate)))

        lines = board + [list(column) for column in zip(*board)]
        reversed_word = word[::-1]
        for line in lines:
            for slot in "".join(line).split("#"):
                if matches(slot, word) or matches(slot, reversed_word):
                    return True
        return False
