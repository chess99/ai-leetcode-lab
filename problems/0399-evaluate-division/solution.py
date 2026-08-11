# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:52:42Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict, deque
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (first, second), value in zip(equations, values): graph[first].append((second, value)); graph[second].append((first, 1 / value))
        result = []
        for start, end in queries:
            if start not in graph or end not in graph: result.append(-1.0); continue
            queue = deque([(start, 1.0)]); seen = {start}; answer = -1.0
            while queue:
                node, product = queue.popleft()
                if node == end: answer = product; break
                for neighbor, weight in graph[node]:
                    if neighbor not in seen: seen.add(neighbor); queue.append((neighbor, product * weight))
            result.append(answer)
        return result
