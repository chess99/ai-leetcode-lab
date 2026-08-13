# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:01:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        return [shorter * (k - long_count) + longer * long_count for long_count in range(k + 1)]
