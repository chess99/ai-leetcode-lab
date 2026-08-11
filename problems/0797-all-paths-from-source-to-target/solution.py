# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:46:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        def dfs(node, path):
            if node == len(graph)-1: result.append(path); return
            for nxt in graph[node]: dfs(nxt, path + [nxt])
        dfs(0, [0]); return result
