# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:10:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts = [0] * 60
        pairs = 0
        for duration in time:
            remainder = duration % 60
            pairs += counts[(-remainder) % 60]
            counts[remainder] += 1
        return pairs
