# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:29:05Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import List, Optional


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ids, counts, duplicates = {}, defaultdict(int), []
        node_ids = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
                continue
            key = (node.val, node_ids.get(node.left, 0), node_ids.get(node.right, 0))
            if key not in ids:
                ids[key] = len(ids) + 1
            node_id = ids[key]
            node_ids[node] = node_id
            counts[node_id] += 1
            if counts[node_id] == 2:
                duplicates.append(node)
        return duplicates
