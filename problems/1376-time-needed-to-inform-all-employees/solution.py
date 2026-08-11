# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:08Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        subordinates = [[] for _ in range(n)]
        for employee, supervisor in enumerate(manager):
            if supervisor != -1:
                subordinates[supervisor].append(employee)

        queue = deque([(headID, 0)])
        total_time = 0
        while queue:
            employee, received_at = queue.popleft()
            total_time = max(total_time, received_at)
            notified_at = received_at + informTime[employee]
            for subordinate in subordinates[employee]:
                queue.append((subordinate, notified_at))

        return total_time
