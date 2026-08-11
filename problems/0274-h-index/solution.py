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
        citations.sort(reverse=True)
        for index, count in enumerate(citations, start=1):
            if count < index: return index - 1
        return len(citations)
