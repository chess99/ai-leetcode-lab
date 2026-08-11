# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def distances_from(start: int) -> List[int]:
            distances = [-1] * len(edges)
            distance = 0
            node = start

            while node != -1 and distances[node] == -1:
                distances[node] = distance
                distance += 1
                node = edges[node]

            return distances

        first_distances = distances_from(node1)
        second_distances = distances_from(node2)
        answer = -1
        best_distance = len(edges) + 1

        for node in range(len(edges)):
            if first_distances[node] == -1 or second_distances[node] == -1:
                continue

            maximum_distance = max(
                first_distances[node],
                second_distances[node],
            )
            if maximum_distance < best_distance:
                best_distance = maximum_distance
                answer = node

        return answer
