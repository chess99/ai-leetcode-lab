# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:44:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        return all(abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) > distance
                   for ghost in ghosts)
