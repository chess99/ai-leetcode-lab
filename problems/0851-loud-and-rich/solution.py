# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:38Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph=[[] for _ in quiet]
        for rich, poor in richer: graph[poor].append(rich)
        @lru_cache(None)
        def dfs(person):
            best=person
            for rich in graph[person]:
                candidate=dfs(rich)
                if quiet[candidate]<quiet[best]: best=candidate
            return best
        return [dfs(i) for i in range(len(quiet))]
