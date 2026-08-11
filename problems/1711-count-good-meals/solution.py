# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:32Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        seen = Counter()
        pairs = 0
        modulo = 1_000_000_007

        for value in deliciousness:
            for power in range(22):
                pairs += seen[(1 << power) - value]
            seen[value] += 1

        return pairs % modulo
