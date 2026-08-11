# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:12Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counts = defaultdict(int)
        pairs = 0

        for width, height in rectangles:
            divisor = gcd(width, height)
            ratio = (width // divisor, height // divisor)
            pairs += counts[ratio]
            counts[ratio] += 1

        return pairs
