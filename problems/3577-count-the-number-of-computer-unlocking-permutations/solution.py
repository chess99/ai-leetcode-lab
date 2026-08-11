# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if any(value <= complexity[0] for value in complexity[1:]): return 0
        ans = 1
        for x in range(2, len(complexity)):
            ans = ans * x % 1_000_000_007
        return ans
