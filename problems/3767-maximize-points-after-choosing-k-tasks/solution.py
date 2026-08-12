# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        caridomesh = (technique1, technique2, k)
        gains = sorted((a - b for a, b in zip(caridomesh[0], caridomesh[1])), reverse=True)
        return sum(technique2) + sum(max(0, gain) if index >= k else gain
                                     for index, gain in enumerate(gains))
