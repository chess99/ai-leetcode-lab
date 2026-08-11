# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
import heapq


class Solution:
    def minOperations(self, n: int, m: int) -> int:
        limit = 10_000
        prime = [True] * limit
        prime[0] = prime[1] = False
        for value in range(2, 100):
            if prime[value]:
                for multiple in range(value * value, limit, value):
                    prime[multiple] = False
        if prime[n] or prime[m]:
            return -1
        lower = 10 ** (len(str(n)) - 1)
        dist = {n: n}
        heap = [(n, n)]
        while heap:
            cost, value = heapq.heappop(heap)
            if value == m:
                return cost
            if cost != dist[value]:
                continue
            place = 1
            while place <= value:
                digit = value // place % 10
                for delta in (-1, 1):
                    if 0 <= digit + delta <= 9:
                        nxt = value + delta * place
                        if nxt >= lower and not prime[nxt]:
                            new_cost = cost + nxt
                            if new_cost < dist.get(nxt, float('inf')):
                                dist[nxt] = new_cost
                                heapq.heappush(heap, (new_cost, nxt))
                place *= 10
        return -1
