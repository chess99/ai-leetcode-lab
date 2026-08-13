# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:40Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val, self.left, self.right = x, None, None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        def link(node):
            if node:
                if node.left: parents[node.left] = node
                if node.right: parents[node.right] = node
                link(node.left); link(node.right)
        link(root)
        queue = deque([(target, 0)])
        seen = {target}
        result = []
        while queue:
            node, distance = queue.popleft()
            if distance == k: result.append(node.val); continue
            for neighbor in (node.left, node.right, parents.get(node)):
                if neighbor and neighbor not in seen:
                    seen.add(neighbor); queue.append((neighbor, distance + 1))
        return result
