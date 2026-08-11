# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:43:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maximum = chunks = 0
        for index, value in enumerate(arr):
            maximum = max(maximum, value)
            if maximum == index: chunks += 1
        return chunks
