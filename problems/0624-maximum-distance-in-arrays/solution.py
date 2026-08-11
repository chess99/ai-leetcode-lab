# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:26:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum, maximum = arrays[0][0], arrays[0][-1]
        answer = 0
        for array in arrays[1:]:
            answer = max(answer, array[-1] - minimum, maximum - array[0])
            minimum = min(minimum, array[0])
            maximum = max(maximum, array[-1])
        return answer
