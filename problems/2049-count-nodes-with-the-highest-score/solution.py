# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in parents]
        for node in range(1, n):
            children[parents[node]].append(node)

        order = [0]
        for node in order:
            order.extend(children[node])

        subtree_size = [1] * n
        highest_score = 0
        highest_count = 0
        for node in reversed(order):
            for child in children[node]:
                subtree_size[node] += subtree_size[child]

            score = n - subtree_size[node]
            if score == 0:
                score = 1
            for child in children[node]:
                score *= subtree_size[child]

            if score > highest_score:
                highest_score = score
                highest_count = 1
            elif score == highest_score:
                highest_count += 1
        return highest_count
