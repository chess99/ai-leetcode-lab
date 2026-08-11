# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:44:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right, length = 0, len(citations) - 1, len(citations)
        while left <= right:
            middle = (left + right) // 2
            if citations[middle] >= length - middle: right = middle - 1
            else: left = middle + 1
        return length - left
