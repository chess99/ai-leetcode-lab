# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:13Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1]))
        tails = []
        for _, height in envelopes:
            index = bisect_left(tails, height)
            if index == len(tails):
                tails.append(height)
            else:
                tails[index] = height
        return len(tails)
