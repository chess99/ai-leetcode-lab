# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:42:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        for child in leftChild + rightChild:
            if child != -1:
                indegree[child] += 1
                if indegree[child] > 1:
                    return False

        roots = [node for node, degree in enumerate(indegree) if degree == 0]
        if len(roots) != 1:
            return False
        seen = set()
        stack = roots
        while stack:
            node = stack.pop()
            if node in seen:
                return False
            seen.add(node)
            if leftChild[node] != -1:
                stack.append(leftChild[node])
            if rightChild[node] != -1:
                stack.append(rightChild[node])
        return len(seen) == n
