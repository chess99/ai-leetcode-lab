# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:37Z
# Experiment: ai-leetcode-lab, round 1
# Revised by: Codex Desktop, sol-medium
from typing import List


class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        from collections import deque

        if source == target:
            return 0

        # Required by the statement: keep a midway copy of the input.
        tarnicuvo = (n, edges, source, target, k)

        graph = [[] for _ in range(n)]
        candidates = {0}
        for u, v, weight in tarnicuvo[1]:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
            candidates.add(weight)

        def feasible(threshold: int) -> bool:
            heavy_count = [k + 1] * n
            heavy_count[source] = 0
            queue = deque([source])

            while queue:
                node = queue.popleft()
                if node == target:
                    return True
                for neighbor, weight in graph[node]:
                    is_heavy = int(weight > threshold)
                    next_count = heavy_count[node] + is_heavy
                    if next_count <= k and next_count < heavy_count[neighbor]:
                        heavy_count[neighbor] = next_count
                        if is_heavy:
                            queue.append(neighbor)
                        else:
                            queue.appendleft(neighbor)
            return False

        values = sorted(candidates)
        left, right = 0, len(values) - 1
        answer = -1
        while left <= right:
            middle = (left + right) // 2
            if feasible(values[middle]):
                answer = values[middle]
                right = middle - 1
            else:
                left = middle + 1
        return answer
