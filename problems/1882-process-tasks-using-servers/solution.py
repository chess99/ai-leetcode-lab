# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:38Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(weight, index) for index, weight in enumerate(servers)]
        heapq.heapify(available)
        busy = []
        assigned = []
        time = 0

        for task_index, duration in enumerate(tasks):
            time = max(time, task_index)
            while busy and busy[0][0] <= time:
                _, weight, server_index = heapq.heappop(busy)
                heapq.heappush(available, (weight, server_index))

            if not available:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    _, weight, server_index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, server_index))

            weight, server_index = heapq.heappop(available)
            assigned.append(server_index)
            heapq.heappush(busy, (time + duration, weight, server_index))

        return assigned
