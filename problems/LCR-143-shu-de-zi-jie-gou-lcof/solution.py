# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:33Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubStructure(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
        if not A or not B:
            return False

        def match(first, second):
            pairs = [(first, second)]
            while pairs:
                node_a, node_b = pairs.pop()
                if not node_b:
                    continue
                if not node_a or node_a.val != node_b.val:
                    return False
                pairs.append((node_a.left, node_b.left))
                pairs.append((node_a.right, node_b.right))
            return True

        candidates = [A]
        while candidates:
            node = candidates.pop()
            if node.val == B.val and match(node, B):
                return True
            if node.left:
                candidates.append(node.left)
            if node.right:
                candidates.append(node.right)
        return False
