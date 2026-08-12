# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:44Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degree = [0] * n
        shared = Counter()
        for first, second in edges:
            first -= 1
            second -= 1
            degree[first] += 1
            degree[second] += 1
            if first > second:
                first, second = second, first
            shared[first, second] += 1
        ordered = sorted(degree)
        answer = []
        for query in queries:
            count = 0
            left, right = 0, n - 1
            while left < right:
                if ordered[left] + ordered[right] > query:
                    count += right - left
                    right -= 1
                else:
                    left += 1
            for (first, second), overlap in shared.items():
                total = degree[first] + degree[second]
                if total > query and total - overlap <= query:
                    count -= 1
            answer.append(count)
        return answer
