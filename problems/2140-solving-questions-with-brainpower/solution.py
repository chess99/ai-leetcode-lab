# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        best = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_index = min(n, i + brainpower + 1)
            best[i] = max(best[i + 1], points + best[next_index])
        return best[0]
