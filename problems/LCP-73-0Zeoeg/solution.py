# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def adventureCamp(self, expeditions: List[str]) -> int:
        known = set(expeditions[0].split('->')) if expeditions[0] else set()
        best_index = -1
        best_count = 0
        for index in range(1, len(expeditions)):
            camps = set(expeditions[index].split('->')) if expeditions[index] else set()
            new_camps = camps - known
            if len(new_camps) > best_count:
                best_count = len(new_camps)
                best_index = index
            known.update(camps)
        return best_index
