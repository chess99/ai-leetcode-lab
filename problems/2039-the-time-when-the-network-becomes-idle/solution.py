# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:18Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = [[] for _ in patience]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        distance = [-1] * len(patience)
        distance[0] = 0
        queue = deque([0])
        while queue:
            server = queue.popleft()
            for neighbor in graph[server]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[server] + 1
                    queue.append(neighbor)

        last_reply = 0
        for server in range(1, len(patience)):
            round_trip = 2 * distance[server]
            last_sent = ((round_trip - 1) // patience[server]) * patience[server]
            last_reply = max(last_reply, last_sent + round_trip)
        return last_reply + 1
