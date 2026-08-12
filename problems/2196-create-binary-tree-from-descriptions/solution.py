# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:15Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from __future__ import annotations

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent_value, child_value, is_left in descriptions:
            if parent_value not in nodes:
                nodes[parent_value] = TreeNode(parent_value)
            if child_value not in nodes:
                nodes[child_value] = TreeNode(child_value)

            if is_left:
                nodes[parent_value].left = nodes[child_value]
            else:
                nodes[parent_value].right = nodes[child_value]
            children.add(child_value)

        root_value = next(value for value in nodes if value not in children)
        return nodes[root_value]
