# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for caller, callee in invocations:
            graph[caller].append(callee)
        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])
        while queue:
            method = queue.popleft()
            for called in graph[method]:
                if not suspicious[called]:
                    suspicious[called] = True
                    queue.append(called)
        for caller, callee in invocations:
            if not suspicious[caller] and suspicious[callee]:
                return list(range(n))
        return [method for method in range(n) if not suspicious[method]]
