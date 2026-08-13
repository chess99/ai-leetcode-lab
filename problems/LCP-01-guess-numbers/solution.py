# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:24:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(a == b for a, b in zip(guess, answer))
