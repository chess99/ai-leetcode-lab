# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        last, second_last = -1, -1
        answer = 0
        for left, right in sorted(intervals, key=lambda interval: (interval[1], -interval[0])):
            if left > last:
                answer += 2
                second_last, last = right - 1, right
            elif left > second_last:
                answer += 1
                second_last, last = last, right
        return answer
