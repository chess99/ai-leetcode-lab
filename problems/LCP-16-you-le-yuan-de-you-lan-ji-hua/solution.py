# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: high
# Profile: sol-high
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxWeight(self, edges: List[List[int]], value: List[int]) -> int:
        n = len(value)
        degree = [0] * n
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

        # Orient every edge from the smaller (degree, id) endpoint to the
        # larger one. Every triangle is then found exactly once.
        out = [[] for _ in range(n)]
        for u, v in edges:
            if (degree[u], u) > (degree[v], v):
                u, v = v, u
            out[u].append(v)

        triangle_edges = [[] for _ in range(n)]
        marked = [False] * n
        for a in range(n):
            for b in out[a]:
                marked[b] = True
            for b in out[a]:
                for c in out[b]:
                    if marked[c]:
                        triangle_edges[a].append((b, c))
                        triangle_edges[b].append((a, c))
                        triangle_edges[c].append((a, b))
            for b in out[a]:
                marked[b] = False

        answer = 0
        for center, local_edges in enumerate(triangle_edges):
            if not local_edges:
                continue

            # One triangle (the same route may be selected twice).
            best = max(value[u] + value[v] for u, v in local_edges)

            # Two triangle edges sharing one non-center endpoint.
            top_two = {}
            for u, v in local_edges:
                pair = top_two.get(u, (-1, -1))
                x = value[v]
                top_two[u] = (max(pair[0], x), min(pair[0], max(pair[1], x)))
                pair = top_two.get(v, (-1, -1))
                x = value[u]
                top_two[v] = (max(pair[0], x), min(pair[0], max(pair[1], x)))
            for u, (first, second) in top_two.items():
                if second >= 0:
                    best = max(best, value[u] + first + second)

            # Two disjoint edges form four distinct non-center projects.
            ordered = sorted(
                local_edges, key=lambda e: value[e[0]] + value[e[1]], reverse=True
            )
            best_without = {}

            def without(vertex: int):
                if vertex not in best_without:
                    best_without[vertex] = next(
                        (e for e in ordered if vertex not in e), None
                    )
                return best_without[vertex]

            for u, v in local_edges:
                candidate = without(u)
                if candidate is not None and v not in candidate:
                    other = candidate
                else:
                    candidate = without(v)
                    if candidate is not None and u not in candidate:
                        other = candidate
                    else:
                        other = next(
                            (e for e in ordered if u not in e and v not in e), None
                        )
                if other is not None:
                    best = max(
                        best,
                        value[u] + value[v] + value[other[0]] + value[other[1]],
                    )

            answer = max(answer, value[center] + best)
        return answer
