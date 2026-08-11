# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        def amounts(start, pairs, rates):
            graph = defaultdict(list)
            for (a, b), rate in zip(pairs, rates):
                graph[a].append((b, rate))
                graph[b].append((a, 1 / rate))
            best, stack = {start: 1.0}, [start]
            while stack:
                cur = stack.pop()
                for nxt, rate in graph[cur]:
                    if nxt not in best:
                        best[nxt] = best[cur] * rate
                        stack.append(nxt)
            return best
        first = amounts(initialCurrency, pairs1, rates1)
        second = amounts(initialCurrency, pairs2, rates2)
        return max(value / second[currency] for currency, value in first.items() if currency in second)
