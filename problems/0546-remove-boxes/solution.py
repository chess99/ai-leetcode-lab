# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:18Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def score(left, right, carried):
            if left > right:
                return 0
            while left < right and boxes[right] == boxes[right - 1]:
                right -= 1
                carried += 1
            answer = score(left, right - 1, 0) + (carried + 1) ** 2
            for middle in range(left, right):
                if boxes[middle] == boxes[right]:
                    answer = max(answer, score(left, middle, carried + 1)
                                 + score(middle + 1, right - 1, 0))
            return answer
        return score(0, len(boxes) - 1, 0)
