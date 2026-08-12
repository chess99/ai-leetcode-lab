# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:32Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        waiting_left = []
        waiting_right = []
        working_left = []
        working_right = []
        for worker, (left_to_right, _, right_to_left, _) in enumerate(time):
            heapq.heappush(waiting_left, (-(left_to_right + right_to_left), -worker))

        current = 0
        remaining = n
        while remaining or waiting_right or working_right:
            while working_left and working_left[0][0] <= current:
                _, worker = heapq.heappop(working_left)
                heapq.heappush(
                    waiting_left,
                    (-(time[worker][0] + time[worker][2]), -worker),
                )
            while working_right and working_right[0][0] <= current:
                _, worker = heapq.heappop(working_right)
                heapq.heappush(
                    waiting_right,
                    (-(time[worker][0] + time[worker][2]), -worker),
                )

            if waiting_right:
                _, negative_worker = heapq.heappop(waiting_right)
                worker = -negative_worker
                current += time[worker][2]
                heapq.heappush(working_left, (current + time[worker][3], worker))
            elif remaining and waiting_left:
                _, negative_worker = heapq.heappop(waiting_left)
                worker = -negative_worker
                current += time[worker][0]
                remaining -= 1
                heapq.heappush(working_right, (current + time[worker][1], worker))
            else:
                next_times = []
                if working_left:
                    next_times.append(working_left[0][0])
                if working_right:
                    next_times.append(working_right[0][0])
                current = min(next_times)
        return current
