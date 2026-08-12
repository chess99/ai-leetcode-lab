# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:48Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        queue = []
        columns = len(values[0])
        for row in range(len(values)):
            heapq.heappush(queue, (values[row][-1], row, columns - 1))
        answer = 0
        day = 1
        while queue:
            value, row, column = heapq.heappop(queue)
            answer += day * value
            day += 1
            if column:
                heapq.heappush(queue, (values[row][column - 1], row, column - 1))
        return answer
