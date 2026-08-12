# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph=[[] for _ in range(n)]
        for a,b in edges:graph[a].append(b);graph[b].append(a)
        answer = [0] * n
        label_counts = [0] * 26
        counts_before_subtree = [0] * n
        stack = [(0, -1, False)]

        while stack:
            node, parent, exiting = stack.pop()
            label = ord(labels[node]) - ord("a")
            if not exiting:
                counts_before_subtree[node] = label_counts[label]
                stack.append((node, parent, True))
                for child in graph[node]:
                    if child != parent:
                        stack.append((child, node, False))
            else:
                label_counts[label] += 1
                answer[node] = label_counts[label] - counts_before_subtree[node]

        return answer
