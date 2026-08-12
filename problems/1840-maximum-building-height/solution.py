# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        limits = [[1, 0]] + sorted(restrictions)
        if not limits or limits[-1][0] != n:
            limits.append([n, n - 1])
        for index in range(1, len(limits)):
            distance = limits[index][0] - limits[index - 1][0]
            limits[index][1] = min(limits[index][1],
                                   limits[index - 1][1] + distance)
        for index in range(len(limits) - 2, -1, -1):
            distance = limits[index + 1][0] - limits[index][0]
            limits[index][1] = min(limits[index][1],
                                   limits[index + 1][1] + distance)
        answer = 0
        for (left, left_height), (right, right_height) in zip(limits, limits[1:]):
            distance = right - left
            peak = (left_height + right_height + distance) // 2
            answer = max(answer, peak)
        return answer
