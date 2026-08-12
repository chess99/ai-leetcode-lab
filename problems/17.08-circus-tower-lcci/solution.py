# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:49Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        people = sorted(zip(height, weight), key=lambda person: (person[0], -person[1]))
        tails = []
        for _, current_weight in people:
            index = bisect_left(tails, current_weight)
            if index == len(tails):
                tails.append(current_weight)
            else:
                tails[index] = current_weight
        return len(tails)
