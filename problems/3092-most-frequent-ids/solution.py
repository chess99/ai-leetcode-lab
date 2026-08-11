# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        import heapq
        from collections import defaultdict

        counts = defaultdict(int)
        heap = []
        answer = []
        for identifier, delta in zip(nums, freq):
            counts[identifier] += delta
            heapq.heappush(heap, (-counts[identifier], identifier))
            while heap and -heap[0][0] != counts[heap[0][1]]:
                heapq.heappop(heap)
            answer.append(-heap[0][0] if heap else 0)
        return answer
