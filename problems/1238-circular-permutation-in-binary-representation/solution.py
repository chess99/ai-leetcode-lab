# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:29:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ (value ^ (value >> 1)) for value in range(1 << n)]
