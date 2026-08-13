# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:10Z
# Experiment: ai-leetcode-lab, round 1

from collections import defaultdict, deque
from typing import Optional




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        stack = [root]

        while stack:
            node = stack.pop()
            for child in (node.left, node.right):
                if child:
                    graph[node.val].append(child.val)
                    graph[child.val].append(node.val)
                    stack.append(child)

        queue = deque([(start, 0)])
        visited = {start}
        minutes = 0
        while queue:
            node, minutes = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, minutes + 1))

        return minutes
