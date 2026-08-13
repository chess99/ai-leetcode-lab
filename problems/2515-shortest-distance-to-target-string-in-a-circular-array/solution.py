# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:05:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        distances = [min((i-startIndex) % n, (startIndex-i) % n)
                     for i, word in enumerate(words) if word == target]
        return min(distances, default=-1)
