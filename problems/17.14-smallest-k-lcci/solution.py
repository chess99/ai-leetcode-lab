# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:46Z
# Experiment: ai-leetcode-lab, round 1
from heapq import nsmallest
from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return nsmallest(k, arr)
