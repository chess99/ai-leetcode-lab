# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:07:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        counts = [0, 0]
        index = 0
        while n:
            counts[index % 2] += n & 1
            n >>= 1
            index += 1
        return counts
