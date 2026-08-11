# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:33Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending = sorted((enqueue, processing, index) for index, (enqueue, processing) in enumerate(tasks))
        available = []
        order = []
        time = 0
        next_task = 0

        while next_task < len(pending) or available:
            if not available:
                time = max(time, pending[next_task][0])

            while next_task < len(pending) and pending[next_task][0] <= time:
                _, processing, index = pending[next_task]
                heapq.heappush(available, (processing, index))
                next_task += 1

            processing, index = heapq.heappop(available)
            order.append(index)
            time += processing

        return order
