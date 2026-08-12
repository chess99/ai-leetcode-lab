# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:49Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        pending = [[] for _ in heights]
        answer = [-1] * len(queries)
        for index, (first, second) in enumerate(queries):
            if first > second:
                first, second = second, first
            if first == second or heights[first] < heights[second]:
                answer[index] = second
            else:
                pending[second].append((heights[first], index))
        queue = []
        for building, height in enumerate(heights):
            for required, query_index in pending[building]:
                heapq.heappush(queue, (required, query_index))
            while queue and queue[0][0] < height:
                _, query_index = heapq.heappop(queue)
                answer[query_index] = building
        return answer
