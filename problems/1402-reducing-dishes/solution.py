# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        suffix = answer = 0
        for value in sorted(satisfaction, reverse=True):
            if suffix + value <= 0:
                break
            suffix += value
            answer += suffix
        return answer
