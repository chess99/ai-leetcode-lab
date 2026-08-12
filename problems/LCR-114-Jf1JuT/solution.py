# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:27Z
# Experiment: ai-leetcode-lab, round 1
from heapq import heappop, heappush
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}
        indegree = {char: 0 for char in graph}
        for first, second in zip(words, words[1:]):
            if len(first) > len(second) and first.startswith(second):
                return ''
            for a, b in zip(first, second):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break
        heap = []
        for char, degree in indegree.items():
            if degree == 0:
                heappush(heap, char)
        answer = []
        while heap:
            char = heappop(heap)
            answer.append(char)
            for other in graph[char]:
                indegree[other] -= 1
                if indegree[other] == 0:
                    heappush(heap, other)
        return ''.join(answer) if len(answer) == len(graph) else ''
