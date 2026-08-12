# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:52Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = list(range(n))
        heapq.heapify(available)
        occupied = []
        counts = [0] * n
        for start, end in sorted(meetings):
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)
            duration = end - start
            if available:
                room = heapq.heappop(available)
                finish = end
            else:
                finish, room = heapq.heappop(occupied)
                finish += duration
            counts[room] += 1
            heapq.heappush(occupied, (finish, room))
        return max(range(n), key=lambda room: counts[room])
