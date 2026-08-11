# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:27:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda pair: pair[1])
        chain_end = float("-inf")
        length = 0
        for left, right in pairs:
            if left > chain_end:
                length += 1
                chain_end = right
        return length
