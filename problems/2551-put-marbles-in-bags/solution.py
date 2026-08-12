# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        boundaries = sorted(
            weights[index] + weights[index + 1]
            for index in range(len(weights) - 1)
        )
        cuts = k - 1
        return sum(boundaries[-cuts:]) - sum(boundaries[:cuts]) if cuts else 0
