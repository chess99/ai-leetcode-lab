# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [
            index
            for index in range(1, len(mountain) - 1)
            if mountain[index] > mountain[index - 1] and mountain[index] > mountain[index + 1]
        ]
