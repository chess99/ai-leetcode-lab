# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:01:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        exact = sum(expected == actual for expected, actual in zip(solution, guess))
        common = sum(min(solution.count(color), guess.count(color)) for color in 'RGBY')
        return [exact, common - exact]
