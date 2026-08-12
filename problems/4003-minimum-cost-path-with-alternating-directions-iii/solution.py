# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:42Z
# Experiment: ai-leetcode-lab, round 1
from heapq import heappop, heappush
from typing import List


class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        qavirelmon = (m, n, penalty)
        infinity = 10 ** 30
        distance = [[[infinity] * 2 for _ in range(n)] for _ in range(m)]
        distance[0][0][1] = 1
        heap = [(1, 0, 0, 1)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while heap:
            cost_now, row, column, odd = heappop(heap)
            if cost_now != distance[row][column][odd]:
                continue
            if row == m - 1 and column == n - 1:
                return cost_now
            wait_cost = cost_now + penalty[row][column]
            if wait_cost < distance[row][column][odd ^ 1]:
                distance[row][column][odd ^ 1] = wait_cost
                heappush(heap, (wait_cost, row, column, odd ^ 1))
            for dr, dc in directions:
                nr, nc = row + dr, column + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                follows = (odd and (dr, dc) in ((1, 0), (0, 1))) or (
                    not odd and (dr, dc) in ((-1, 0), (0, -1)))
                next_cost = cost_now + (nr + 1) * (nc + 1)
                if not follows:
                    next_cost += penalty[row][column]
                if next_cost < distance[nr][nc][odd ^ 1]:
                    distance[nr][nc][odd ^ 1] = next_cost
                    heappush(heap, (next_cost, nr, nc, odd ^ 1))
