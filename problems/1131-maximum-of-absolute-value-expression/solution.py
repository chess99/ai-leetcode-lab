# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:23:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        answer = 0
        for sign1, sign2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            values = [sign1 * first + sign2 * second + index
                      for index, (first, second) in enumerate(zip(arr1, arr2))]
            answer = max(answer, max(values) - min(values))
        return answer
