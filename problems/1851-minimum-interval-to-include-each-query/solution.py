# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:48Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        answer = {}
        heap = []
        index = 0
        for query in sorted(set(queries)):
            while index < len(intervals) and intervals[index][0] <= query:
                left, right = intervals[index]
                heapq.heappush(heap, (right - left + 1, right))
                index += 1
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            answer[query] = heap[0][0] if heap else -1
        return [answer[query] for query in queries]
