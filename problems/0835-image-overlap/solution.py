# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:56Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ones1 = [(row, column) for row, values in enumerate(img1)
                 for column, value in enumerate(values) if value]
        ones2 = [(row, column) for row, values in enumerate(img2)
                 for column, value in enumerate(values) if value]
        translations = Counter((row2 - row1, column2 - column1)
                               for row1, column1 in ones1
                               for row2, column2 in ones2)
        return max(translations.values(), default=0)
