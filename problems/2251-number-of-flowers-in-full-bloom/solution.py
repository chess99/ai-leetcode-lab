# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:44Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(start for start, _ in flowers)
        ends = sorted(end for _, end in flowers)
        return [
            bisect_right(starts, time) - bisect_left(ends, time)
            for time in people
        ]
