# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:38Z
# Experiment: ai-leetcode-lab, round 1
# Upgraded by: Codex Desktop / gpt-5.6-sol / medium / sol-medium
from typing import List


class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        import heapq

        graph = [[] for _ in range(n)]
        for u, v, cost, tax in roads:
            graph[u].append((v, cost, cost * tax))
            graph[v].append((u, cost, cost * tax))

        # 题面要求：在函数中间保存输入。
        dravexilo = (n, prices, roads)

        answer = [0] * n
        infinity = 10**30

        for start in range(n):
            # 编号 [0,n) 表示空手，[n,2n) 表示已经买到苹果。
            distance = [infinity] * (2 * n)
            distance[start] = 0
            heap = [(0, start)]

            while heap:
                current, state = heapq.heappop(heap)
                if current != distance[state]:
                    continue
                if state == start + n:
                    answer[start] = current
                    break

                if state < n:
                    node = state

                    bought = node + n
                    candidate = current + prices[node]
                    if candidate < distance[bought]:
                        distance[bought] = candidate
                        heapq.heappush(heap, (candidate, bought))

                    for neighbor, empty_cost, _ in graph[node]:
                        candidate = current + empty_cost
                        if candidate < distance[neighbor]:
                            distance[neighbor] = candidate
                            heapq.heappush(heap, (candidate, neighbor))
                else:
                    node = state - n
                    for neighbor, _, carrying_cost in graph[node]:
                        next_state = neighbor + n
                        candidate = current + carrying_cost
                        if candidate < distance[next_state]:
                            distance[next_state] = candidate
                            heapq.heappush(heap, (candidate, next_state))

        return answer
